#!/usr/bin/env python
#########################################
### tools to handle plots
###     compare plots
###     stack plots
###     ratio plots
###   mixture of above
###
###  Author: Huaqiao ZHANG  
###  First version: Apr. 2013 @ MSU
###  Contact: huaqiao.zhang@cern.ch
#########################################
#   class plotsSetting
#           def __init__(self):
#           def autoSetYaxisRange(self, histList):
#           def autoSetLegend(self, histList,opt="FullSize",legMaxRow=15,reverse=1):
#           def drawRatio(self, thisCanvas, hist, opt="hist"):
#           def drawHist(self, thisCanvas, hist, opt="hist"):
#           def stackPlot(self, thisCanvas, stackHistList, histNameList,option="hist"):
#           def compareShapeAndNorm(self, thisCanvas, histList, histNameList):
#           def ratioOfShapeAndNorm(self, thisCanvas, histList):
#           def compareShapeAndNormWithRatio(self, thisCanvas, histList, histNameList):
#           def stackPlotCompareData(self, thisCanvas, stackHistList, histNameList, dataHistList, dataNameList):
#           def stackPlotCompareDataWithRatio(self, thisCanvas, stackHistList, histNameList, dataHistList, dataNameList):
#   def AdjustLabels(hist,option):
#   def AdjustCanvas(thisCanvas):
#   def addUnderFlowAndOverFlow(histList): 
#   def normalizeHist(histList):
#   def selfDivideHist(histList):
#   def addHist(histList):
#########################################
import os
import sys
currentPath = os.getcwd()
sys.path.append( currentPath +"/../"+"utils")
sys.path.append( currentPath +"/../"+"settings")
sys.path.append( currentPath +"/../"+"styles")
from ROOT import *
from math import *
SetAtlasStyle()

class plotsSetting:
    ############ init function set the default settings for the plots
    def __init__(self):
        self.colorList       = [2,3,4, 618, 801, 796, 400, 634, 857]
        self.stackColorList  = [618, 801, 796, 400, 634, 857]
        self.lineStyleList   = [2,3,4,6,7,8,9]
        self.markerStyleList = [21,22,23,25,26,27,28,29]

        self.m_numOfLegColums    = 1 ## legend m_numOfLegColums
        self.m_legXlow  = 0.65
        self.m_legYlow  = 0.65
        self.m_legXhigh = 0.94
        self.m_legYhigh = 0.93
        self.m_legName  = ""

        self.m_logy     = 0
        self.m_YaxisMax_orig = -1e9
        self.m_YaxisMin_orig = 1e9
        self.m_YaxisMax = -1e9
        self.m_YaxisMin = 1e9
        self.m_relativMargin = 0.3

        self.m_XaxisTitle = ""
        self.m_YaxisTitle = "Events"

        self.m_normYaxisTitle = "Events Fraction"

        self.m_ratioYaxisTitle = "Data/Exp."
        self.m_ratioYaxisMax   = 1.4
        self.m_ratioYaxisMin   = 0.6

######################################################################################################################################
#############################  Automatic choose some of the plot settings
    def autoSetYaxisRange(self, histList):
        ymax =-1e9
        ymin = 1e9
        if self.m_YaxisMax_orig>ymax:
            ymax = self.m_YaxisMax_orig
        if self.m_YaxisMin_orig<ymin:
            ymin = self.m_YaxisMin_orig
        ysecondmin = 1e9
        for ihist in histList:
            if ihist.GetBinContent(ihist.GetMaximumBin()) > ymax:
                ymax = ihist.GetBinContent(ihist.GetMaximumBin())
            if ihist.GetBinContent(ihist.GetMinimumBin()) < ymin:
                ymin = ihist.GetBinContent(ihist.GetMinimumBin())
        for ihist in histList:
            for ibin in range(ihist.GetNbinsX()+1):
                if (ihist.GetBinContent(ibin)>ymin) and ihist.GetBinContent(ibin)<ysecondmin:
                    ysecondmin = ihist.GetBinContent(ibin)
        print ("Oringal Ymax, Ymin and second Ymin are: ", ymax, ymin, ysecondmin)
        self.m_YaxisMax_orig = ymax
        self.m_YaxisMin_orig = ymin

        if ymin<=0:
            ymin = ysecondmin/10
        if (self.m_logy==0):
            ymax = ymax+(ymax-ymin)*self.m_relativMargin
        if self.m_logy!=0:
            ymax = ymin*pow(10,log10(ymax/ymin)*(1.+self.m_relativMargin))

        self.m_YaxisMax = ymax
        self.m_YaxisMin = ymin
        print ("Addjusted Ymax and Ymin are: ", ymax, ymin)

    def autoSetLegend(self, histList,opt="FullSize",legMaxRow=15,reverse=1):
        legItem = len(histList) + 1  ### an extra item for the uncertainty
        #print "Legend has ", legItem, " items"
        if legItem%legMaxRow==0:
            self.m_numOfLegColums =  legItem/legMaxRow
        if legItem%legMaxRow!=0:
            self.m_numOfLegColums =  legItem/legMaxRow + 1
        if opt=="FullSize":
            ystep      = 0.055
        elif opt=="upperSize":
            ystep      = 0.075

        xlow = self.m_legXhigh - 0.22 * self.m_numOfLegColums * reverse

        if self.m_numOfLegColums>1:
            if legItem%self.m_numOfLegColums ==0:
                ylow = self.m_legYhigh - ystep * legItem/self.m_numOfLegColums * reverse
            else:
                ylow = self.m_legYhigh - ystep * legItem/self.m_numOfLegColums * reverse + 1
        else:
            ylow = self.m_legYhigh - ystep *legItem * reverse
        self.m_legXlow = xlow
        self.m_legYlow = ylow

######################################################################################################################################
    #### function that draw one ratio histograms  /// with different labels etc
    def drawHist(self, thisCanvas, hist, opt="hist"):
        thisCanvas.cd()
        hist.GetYaxis().SetRangeUser(self.m_YaxisMin,self.m_YaxisMax)
        #hist.GetXaxis().SetTitle(self.m_XaxisTitle)
        #hist.GetYaxis().SetTitle(self.m_YaxisTitle)
        if(self.m_logy==0):
            thisCanvas.SetLogy(0)
        else:
            thisCanvas.SetLogy(1)
        hist.DrawCopy(opt)
        return hist
    #### function that draw one histograms  /// with different labels etc
    def drawRatio(self, thisCanvas, hist, opt="hist"):
        thisCanvas.cd()
        hist.GetYaxis().SetRangeUser(self.m_ratioYaxisMin,self.m_ratioYaxisMax)
        #hist.GetXaxis().SetTitle(self.m_XaxisTitle)
        #hist.GetYaxis().SetTitle(self.m_ratioYaxisTitle)
        hist.DrawCopy(opt)
        return hist
######################################################################################################################################
    #### plots that stack a bounch of histgrams
    def stackPlot(self, thisCanvas, stackHistList, histNameList,option="hist"):
        thisCanvas.cd()
        legend = TLegend(self.m_legXlow,self.m_legYlow,self.m_legXhigh,self.m_legYhigh,"")
        legend.SetNColumns(self.m_numOfLegColums)
        legend.SetTextSize(0.05)
        legend.SetLineColor(0)
        legend.SetFillColor(0)
        legend.SetBorderSize(0)
        if self.m_legName != "":
            legend.SetHeader(self.m_legName)
        if(self.m_logy==0):
            thisCanvas.SetLogy(0)
        else:
            thisCanvas.SetLogy(1)
        tmphist=[]
        m_vecmcbkgcomp = THStack("BackgroundComposition","BackgroundComposition")
        for histIndex in range(len(stackHistList)-1,-1,-1):
            hist = stackHistList[histIndex]
            hist.SetFillColor(hist.GetLineColor())
            tmphist.append(hist.Clone(""))
            m_vecmcbkgcomp.Add(hist.Clone(""))
        for histIndex in range(len(stackHistList)):
            legend.AddEntry(tmphist[histIndex],histNameList[histIndex],"F")
        m_vecmcbkgcomp.Draw(option)
        m_vecmcbkgcomp.GetYaxis().SetTitle(stackHistList[0].GetYaxis().GetTitle());
        m_vecmcbkgcomp.GetXaxis().SetTitle(stackHistList[0].GetXaxis().GetTitle());
        legend.Draw("same")
        thisCanvas.Update()
        return legend,m_vecmcbkgcomp

    #### plots that compare both the shape and rates of a bounch of histgrams
    def compareShapeAndNorm(self, thisCanvas, histList, histNameList):
        thisCanvas.cd()
        legend = TLegend(self.m_legXlow,self.m_legYlow,self.m_legXhigh,self.m_legYhigh,"")
        legend.SetNColumns(self.m_numOfLegColums)
        legend.SetTextSize(0.05)
        legend.SetLineColor(0)
        legend.SetFillColor(0)
        legend.SetBorderSize(0)
        if self.m_legName != "":
            legend.SetHeader(self.m_legName)
        tmphist=[]
        for histIndex in range(len(histList)):
            if histIndex == 0:
                tmphist.append(self.drawHist(thisCanvas,histList[histIndex],"hist").Clone(""))
            else:
                tmphist.append(self.drawHist(thisCanvas,histList[histIndex],"histsame").Clone(""))
            legend.AddEntry(tmphist[histIndex],histNameList[histIndex],"lep")
        legend.Draw("same")
        thisCanvas.Update()
        return legend

    #### plots that compare both the shape and rates of a bounch of ratio histgrams: this first ratio has the error bands on
    def ratioOfShapeAndNorm(self, thisCanvas, histList):
        thisCanvas.cd()
        tmphist=[]
        for histIndex in range(len(histList)):
            histList[histIndex].GetYaxis().SetTitle(self.m_ratioYaxisTitle)
            if histIndex == 0:
                #histList[0].SetFillStyle(0)
                histList[0].SetFillStyle(1001)
                histList[0].SetFillColor(kYellow)
                histList[0].SetMarkerSize(0)
                histList[0].SetLineWidth(0)
                tmphist.append(self.drawRatio(thisCanvas,histList[histIndex],"E2").Clone(""))
                xminR = histList[0].GetBinLowEdge(1);
                xmaxR = histList[0].GetBinLowEdge(histList[0].GetNbinsX()+1);
                line2 = TLine()
                line2.SetLineColor(2);
                line2.DrawLine(xminR,1.,xmaxR,1.);
                line2.Draw()
            else:
                tmphist.append(self.drawRatio(thisCanvas,histList[histIndex],"samehist").Clone(""))
        thisCanvas.Update()

######################################################################################################################################
##############    composite plots
    def compareShapeAndNormWithRatio(self, thisCanvas, histList, histNameList):
        m_pad1,m_padr = AdjustCanvas(thisCanvas)
        m_pad1.cd()
        if self.m_logy:
            m_pad1.SetLogy(1)
        else:
            m_pad1.SetLogy(0)
        for histIndex in range(len(histList)):
            AdjustLabels(histList[histIndex],"upperSize")
        legend = self.compareShapeAndNorm(m_pad1,histList,histNameList)

        m_padr.cd()
        ratioList = selfDivideHist(histList)
        for histIndex in range(len(ratioList)):
            AdjustLabels(ratioList[histIndex],"ratioSize")
        self.ratioOfShapeAndNorm(m_padr,ratioList)
        return legend

    def stackPlotCompareData(self, thisCanvas, stackHistList, histNameList, dataHistList, dataNameList):
        thisCanvas.cd()
        stackTotal      = addHist(stackHistList)
        stackTotal.SetFillColor(1)
        #stackTotal.SetFillStyle(3004)
        stackTotal.SetFillStyle(3354)
        self.drawHist(thisCanvas,stackTotal,"E2")
        legend,vec = self.stackPlot(thisCanvas,stackHistList,histNameList,"samehist")
        self.drawHist(thisCanvas,stackTotal,"sameE2")
        legend.AddEntry(stackTotal,"Uncertainty","F")
        tmphist = []
        for histIndex in range(len(dataHistList)):
            tmphist.append( self.drawHist(thisCanvas,dataHistList[histIndex], "esame").Clone(""))
            legend.AddEntry(tmphist[histIndex],dataNameList[histIndex],"lep")
            print (dataNameList[histIndex],tmphist[histIndex].GetYaxis().GetTitle())
        thisCanvas.Update()
        return legend,vec,stackTotal

    def stackPlotCompareDataWithRatio(self, thisCanvas, stackHistList, histNameList, dataHistList, dataNameList):
        m_pad1,m_padr   = AdjustCanvas(thisCanvas)
        stackTotal      = addHist(stackHistList)
        m_pad1.cd()
        if self.m_logy:
            m_pad1.SetLogy(1)
        else:
            m_pad1.SetLogy(0)
        for histIndex in range(len(dataHistList)):
            AdjustLabels(dataHistList[histIndex],"upperSize")
        for histIndex in range(len(stackHistList)):
            AdjustLabels(stackHistList[histIndex],"upperSize")
        AdjustLabels(stackTotal,"upperSize")
        stackTotal.SetFillColor(1)
        #stackTotal.SetFillStyle(3004)
        stackTotal.SetFillStyle(3354)
        self.drawHist(m_pad1,stackTotal,"E2")
        print (stackHistList,histNameList)
        legend,vec = self.stackPlot(m_pad1,stackHistList,histNameList,"samehist")
        legend.AddEntry(stackTotal,"Uncertainty","F")
        self.drawHist(m_pad1,stackTotal,"sameE2")

        tmphist = []
        for histIndex in range(len(dataHistList)):
            tmphist.append( self.drawHist(m_pad1,dataHistList[histIndex], "esame").Clone(""))
            legend.AddEntry(tmphist[histIndex],dataNameList[histIndex],"lep")

        m_padr.cd()
        compareHistList = []
        compareHistList.append(stackTotal)
        for ifile in dataHistList:
            compareHistList.append(ifile)
        for histIndex in range(len(compareHistList)):
            AdjustLabels(compareHistList[histIndex],"ratioSize")
        ratioList = selfDivideHist(compareHistList)
        self.ratioOfShapeAndNorm(m_padr,ratioList)
        thisCanvas.Update()

        return legend,vec,stackTotal

######################################################################################################################################
########################################## common useful hist functions
def AdjustLabels(hist,option):
    if option=="FullSize":
        return hist
    elif option=="upperSize":
        hist.GetYaxis().SetTitleSize(0.065)
        hist.GetYaxis().SetTitleOffset(0.77)
        hist.GetYaxis().SetLabelSize(0.065)
        return hist
    elif option=="ratioSize":
        yaxisR = hist.GetYaxis()
        xaxisR = hist.GetXaxis()
        xaxisR.SetLabelSize(0.15)
        xaxisR.SetTitleSize(0.15)
        xaxisR.SetTitleOffset(0.95)
        yaxisR.SetNdivisions(504)
        yaxisR.SetLabelSize(0.15)
        yaxisR.SetTitleOffset(0.33)
        yaxisR.SetTitleSize(0.15)
        return hist
    else:
        return hist

def AdjustCanvas(thisCanvas):
    thisCanvas.cd()
    m_pad1 = TPad("m_pad1","data",0.0,0.30,1.0,1.0,10)
    m_pad1.SetBottomMargin(0.003)
    m_pad1.Draw()
    m_pad1.SetTicks(1,1)
    m_pad1.SetLogx(0)
    m_pad1.SetLogy(0)
    thisCanvas.cd()
    m_padr = TPad("m_padr","ratio",0.0,0.0,1.0,0.30,10)
    m_padr.SetTopMargin(0.06)
    m_padr.SetBottomMargin(0.35)
    m_padr.Draw()
    m_padr.SetTicks(1,1)
    m_padr.SetLogx(0)
    m_padr.SetLogy(0)
    return m_pad1,m_padr

def addUnderFlowAndOverFlow(histList): ### be careful about the underflow and overflow
    for ihist in histList:
        ihist.SetBinContent(1,ihist.GetBinContent(1)+ihist.GetBinContent(0))
        ihist.SetBinContent(ihist.GetNbinsX(),ihist.GetBinContent(ihist.GetNbinsX()+1)+ihist.GetBinContent(ihist.GetNbinsX()))

def normalizeHist(histList):
    for ihist in histList:
        #ihist.Sumw2()
        ihist.GetYaxis().SetTitle("Events Fraction")
        total = 0.
        for ibin in range(1,ihist.GetNbinsX()+1):  ### be careful about the underflow and overflow
            total = total + ihist.GetBinContent(ibin)
        if total !=0:
            ihist.Scale(1./total)

def selfDivideHist(histList):
    #### missing sanity check functions here
    ratioList = []
    for ihist in histList:
        ratioHist = ihist.Clone("")
        for ibin in range(1,ihist.GetNbinsX()+1):
            if histList[0].GetBinContent(ibin)!=0:
                ratioHist.SetBinContent(ibin,ihist.GetBinContent(ibin)/histList[0].GetBinContent(ibin))
                if ihist.GetBinContent(ibin)!=0:
                    #print "check error", ibin,ihist.GetBinError(ibin),ihist.GetBinContent(ibin), histList[0].GetBinError(ibin)/histList[0].GetBinContent(ibin)
                    error = sqrt(pow(ihist.GetBinError(ibin)/ihist.GetBinContent(ibin),2) +  pow(histList[0].GetBinError(ibin)/histList[0].GetBinContent(ibin),2))
                else:
                    error = histList[0].GetBinError(ibin)/histList[0].GetBinContent(ibin)
                ratioHist.SetBinError(ibin,error)
            else:
                ratioHist.SetBinContent(ibin,0.)
                ratioHist.SetBinError(ibin,0.)
        ratioList.append(ratioHist.Clone(""))
    return ratioList

def addHist(histList):
    #### missing sanity check functions here
    for histIndex in range(len(histList)):
        if histIndex==0:
            tmpHist = histList[histIndex].Clone("stack")
        else:
            tmpHist.Add(histList[histIndex],1.)
    tmpHist.SetLineColor(1)
    tmpHist.SetLineWidth(0)
    tmpHist.SetMarkerColor(1)
    tmpHist.SetMarkerStyle(20)
    tmpHist.SetMarkerSize(0)
    return tmpHist


######################################################################################################################################
#### Debug codes
####
######################################################################################################################################
if __name__ == '__main__':
    ROOT.gROOT.LoadMacro(currentPath+"/../styles/AtlasStyle.C") 
    infilename = "../inputFile/template_Bstar_lepPt_130-newPDFnewQCDWJETS-ST.root"
    infile  = TFile(infilename)
    allhist = infile.GetListOfKeys()
    hist    = infile.Get("Mu_allJetLeptonMETMass__tW")

    histList = []
    dataList = []
    histNameList = []
    dataNameList = []

    hist1 = hist.Clone("")
    hist1.SetLineColor(kBlue)
    histList.append(hist1)
    histNameList.append("line 1")

    hist2 = hist.Clone("")
    hist2.SetLineColor(kGreen)
    histList.append(hist2)
    dataNameList.append("data 1")

    hist3 = hist.Clone("")
    hist3.SetLineColor(kBlack)
    dataList.append(hist3)
    histNameList.append("line 2")

    hist4 = hist.Clone("")
    hist4.SetLineColor(kRed)
    dataList.append(hist4)
    dataNameList.append("data 2")
    ### Add underflow and overflow into hist/data
    addUnderFlowAndOverFlow(histList)
    addUnderFlowAndOverFlow(dataList)
### normalize all the histgrams
    #normalizeHist(histList)
### plot the plots
    plotCTR = plotsSetting()  ### plots setting class that include all the setting information
    plotCTR.m_logy = 1
    #plotCTR.autoSetLegend(histList)
    plotCTR.autoSetYaxisRange(histList)
    plotCTR.m_XaxisTitle = ""
    plotCTR.m_YaxisTitle = "Events"
    c1      = TCanvas("c1","c1",800,600)
    #legend  = plotCTR.compareShapeAndNorm(c1,histList,histNameList)
    #legend  = plotCTR.compareShapeAndNormWithRatio(c1,histList,histNameList)
    #legend  = plotCTR.stackPlot(c1,histList,histNameList)
    #plotCTR.ratioOfShapeAndNorm(c1,histList)
    #legend,vec,total = plotCTR.stackPlotCompareData(c1,histList,histNameList,dataList,dataNameList)
    legend,vec,total = plotCTR.stackPlotCompareDataWithRatio(c1,histList,histNameList,dataList,dataNameList)
    c1.Update()
    c1.SaveAs("test.gif")


