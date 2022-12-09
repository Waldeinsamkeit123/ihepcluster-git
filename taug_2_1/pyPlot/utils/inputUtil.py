#!/usr/bin/env python
#########################################
### tools to handle input files 
###
###  Author: Huaqiao ZHANG  
###  First version: Apr. 2013 @ MSU
###  Contact: huaqiao.zhang@cern.ch
#########################################
#   class sample:
#       def __init__(self,inFile="",name="",color=1,lineStyle=1,markerStyle=21):
#   class treeVarPlot:
#       def __init__(self,sample="",treeName="",varName="",xmin=0,xmax=100,nBin=25,scale=1,XaxisTitle=""):
#   def getOneHistFromOneFile(infile, histName):
#   def getHistFromFile(infileList, histName):
#   def getYield(sampleList,MCselOpt,dataSelOpt):
#   def getHistFromTree(sampleList,aTreeVarPlot,MCselOpt,dataSelOpt,dataDrivenSelOpt=''):
#   def getNameList(sampleList):
#   def getLegendNameList(sampleList):
#   def saveHistToOneFile(rootFileName, histList,fileNameList,varName,preFix="",postFix="",fileOption="update"):
#########################################
import os
import sys
currentPath = os.getcwd()
sys.path.append( currentPath +"/../"+"utils")
sys.path.append( currentPath +"/../"+"settings")
from ROOT import *
from plotUtil import *

def getOneHistFromOneFile(ifile, histName):
    infile  = TFile(ifile)
    hist    = infile.Get(histName)
    return hist,infile

def getHistFromFile(infileList, histName):
    histList = []
    for ifile in infileList:
        infile  = TFile(ifile)
        hist    = infile.Get(histName)
        histList.append(hist.Clone(""))
    return histList

class sample:
    def __init__(self,inFile="",name="",color=1,lineStyle=1,markerStyle=21,legendName=""):
        self.inFile      = inFile
        self.name        = name
        self.legendName  = legendName
        self.treeName    = "TopTree"
        self.color       = color
        self.lineStyle   = lineStyle
        self.markerStyle = markerStyle
        self.thisYield   = -1
        self.dataType    = "MC"

class treeVarPlot:
    def __init__(self,sample="",treeName="",varName="",xmin=0,xmax=100,nBin=25,scale=1,XaxisTitle=""):
        self.sample = sample
        self.treeName = treeName
        self.varName = varName
        self.xmin = xmin
        self.xmax = xmax
        self.nBin = nBin
        self.scale = scale
        self.XaxisTitle = XaxisTitle
        self.YaxisTitle = "Events"

def getYield(sampleList,MCselOpt,dataSelOpt):
    for isample in sampleList:
        rooFile = TFile(isample.inFile)
        tree = rooFile.Get(isample.treeName)
        tmp = TH1F("tmp","tmp",1,-1000000000000000,10000000000000000000)
        if isample.dataType=="MC":
            tree.Draw("EventNumber>>tmp",MCselOpt,"goff")
        elif isample.dataType=="data":
            tree.Draw("EventNumber>>tmp",dataSelOpt,"goff")
        hist = tmp.Clone("")
        isample.thisYield = hist.Integral()

def getHistFromTree(sampleList,aTreeVarPlot,MCselOpt,dataSelOpt,dataDrivenSelOpt=''):
    histList = []
    rooFile  = []
    #print sampleList
    for isam in range(len(sampleList)):
        isample = sampleList[isam]
        rooFile.append(TFile(isample.inFile))
        print ("Open file : ", isample.inFile)
        tree = rooFile[isam].Get(isample.treeName)
        tmp = TH1F("tmp","tmp",aTreeVarPlot.nBin,aTreeVarPlot.xmin,aTreeVarPlot.xmax)
        tmp.Sumw2()
        if isample.dataType=="MC":
            tree.Draw( aTreeVarPlot.varName+">>tmp", MCselOpt, "goff")
        elif isample.dataType=="data":
            tree.Draw(aTreeVarPlot.varName+">>tmp",dataSelOpt,"goff")
        elif isample.dataType=="dataDriven":
            tree.Draw(aTreeVarPlot.varName+">>tmp",dataDrivenSelOpt,"goff")
        hist = tree.GetHistogram()
        hist.GetYaxis().SetTitle(aTreeVarPlot.YaxisTitle)
        hist.GetXaxis().SetTitle(aTreeVarPlot.XaxisTitle)
        hist.SetLineColor  (isample.color)
        hist.SetLineStyle  (isample.lineStyle)
        hist.SetMarkerColor(isample.color)
        hist.SetMarkerStyle(isample.markerStyle)
        hist.SetTitle(isample.legendName)
        #for ibin in range(1,hist.GetNbinsX()+1):
        #    if hist.GetBinContent(ibin)!=0:
        #        print "check error", ibin,hist.GetBinError(ibin),hist.GetBinContent(ibin), hist.GetBinError(ibin)/hist.GetBinContent(ibin)
        histList.append(hist)
    return histList,rooFile #### return rooFile inorder to access the generated histos

def getNameList(sampleList):
    nameList = []
    for isample in sampleList:
        nameList.append(isample.name)
    return nameList

def getLegendNameList(sampleList):
    nameList = []
    for isample in sampleList:
        nameList.append(isample.legendName)
    return nameList

def saveHistToOneFile(rootFileName, histList,fileNameList,varName,preFix="",postFix="",fileOption="update"):
    if len(histList)!=len(fileNameList):
        print ("Histograms and File Names not match")
        sys.exit()
    outFile  = TFile(rootFileName,fileOption)
    outFile.cd()
    for ihist in range(len(histList)):
        histName = preFix+"_"+fileNameList[ihist]+"_"+varName+"_"+postFix
        histList[ihist].Write(histName,2) # TObject::kOverwrite

def saveHistsToMultiFiles(histList,sampleNameList,varName,preFix="",postFix="",fileOption="recreate"):
    if len(histList)!=len(sampleNameList):
        print ("Histograms and File Names not match")
        sys.exit()
    for ihist in range(len(histList)):
        rootFileName = preFix+"_"+sampleNameList[ihist]+"_"+varName+"_"+postFix+".root"
        outFile  = TFile(rootFileName,fileOption)
        outFile.cd()
        histList[ihist].Write(varName,2) # TObject::kOverwrite
        outFile.Close()

###############################################################################################################################
###  The following are the Debug code
###
###############################################################################################################################

if __name__ == '__main__':
    MCselOpt = ""
    stackSampleList = []
    dataSampleList  = []
    totalSampleList = []
    plotList = []

    Wt = sample(name="Wt",color=kAzure-3,lineStyle=1,markerStyle=21)
    Wt.inFile = "../mergRootOutFile/LP2fb_fake/SingleTop.WtDiAcerMCHW.LP2fb_fake.MC.em1+j.noshift.WtDilepton.rootskimBDT.root"
    stackSampleList.append(Wt);    totalSampleList.append(Wt)
    ttbar = sample(name="t\\bar{t}",color=kRed+2,lineStyle=1,markerStyle=21)
    ttbar.inFile = "../mergRootOutFile/LP2fb_fake/SingleTop.ttMCNLO.LP2fb_fake.MC.em1+j.noshift.WtDilepton.rootskimBDT.root"
    stackSampleList.append(ttbar);    totalSampleList.append(ttbar)

    HT = treeVarPlot(totalSampleList,varName="HT",xmin=0,xmax=1000,scale=1.,nBin=50)
    plotList.append(HT)

    getYield(totalSampleList,MCselOpt)
    #print Wt.thisYield, ttbar.thisYield
    histList,rooFile = getHistFromTree(stackSampleList,plotList[0],MCselOpt)
    histNameList = getLegendNameList(stackSampleList)
    print ("checkHist", histList[0].Integral(), histList[1])
    addUnderFlowAndOverFlow(histList)
    normalizeHist(histList)

    plotCTR = plotsSetting()  ### plots setting class that include all the setting information
    plotCTR.m_logy = 1
    plotCTR.autoSetLegend(histList)
    plotCTR.autoSetYaxisRange(histList)
    plotCTR.m_XaxisTitle = ""
    plotCTR.m_YaxisTitle = "Events"
    c1      = TCanvas("c1","c1",800,600)
    #legend  = plotCTR.compareShapeAndNorm(c1,histList,histNameList)
    legend  = plotCTR.compareShapeAndNormWithRatio(c1,histList,histNameList)
    #legend  = plotCTR.stackPlot(c1,histList,histNameList)
    #plotCTR.ratioOfShapeAndNorm(c1,histList)
    #legend,vec,total = plotCTR.stackPlotCompareData(c1,histList,histNameList,dataList,dataNameList)
    #legend,vec,total = plotCTR.stackPlotCompareDataWithRatio(c1,histList,histNameList,dataList,dataNameList)
    c1.Update()
    c1.SaveAs("test.gif")



