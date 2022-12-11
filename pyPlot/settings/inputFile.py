#!/usr/bin/env python
#########################################
### place to define the input files 
###
###  Author: Huaqiao ZHANG  
###  First version: Apr. 2013 @ MSU
###  Contact: huaqiao.zhang@cern.ch
#########################################
# Data member
#   stackSampleList
#   dataSampleList
#   totalSampleList
#   sysSampleArray
#########################################
import os
from ROOT import *
import sys
currentPath = os.getcwd()
sys.path.append( currentPath +"/../"+"utils")
sys.path.append( currentPath +"/../"+"settings")
from inputUtil import *
from selectionCut import *
########################### common block #############################
stackSampleList = []
dataSampleList  = []
totalSampleList = []
sysSampleArray = {}
#######################################################################
tag = 'GTV27_Aug2014-step2-merged'
inputFilePath = "/publicfs/cms/data/TopQuark/tWsemiLeptonic/"+tag
channel = 'Ele'
#channel = 'Mu'

data2012    = sample(name="data2012",   color=kBlack,       lineStyle=1,    markerStyle=20)
data2012.inFile = inputFilePath+"/"+"Data_"+channel+"_noSyst.root"
data2012.dataType = "data"
data2012.treeName = "Trees"+channel+"/NJets_noSyst"
dataSampleList.append(data2012);   totalSampleList.append(data2012)

Wt          = sample(name="Wt",        legendName="tW",                color=kMagenta,         lineStyle=1,    markerStyle=21)
Wt.treeName = "Trees"+channel+"/NJets_noSyst"
tchannel    = sample(name="tchannel",  legendName="t-Channel",         color=kMagenta+2,       lineStyle=1,    markerStyle=22)
tchannel.treeName = "Trees"+channel+"/NJets_noSyst"
schannel    = sample(name="schannel",  legendName="s-Channel",         color=kMagenta-2,       lineStyle=1,    markerStyle=23)
schannel.treeName = "Trees"+channel+"/NJets_noSyst"
ttbar       = sample(name="ttbar",     legendName="t\\bar{t}",         color=kRed+1,           lineStyle=1,    markerStyle=24)
ttbar.treeName = "Trees"+channel+"/NJets_noSyst"
wjets       = sample(name="wjets",     legendName="W#rightarrowl#nu",  color=kGreen-3,         lineStyle=1,    markerStyle=25)
wjets.treeName = "Trees"+channel+"/NJets_noSyst"
diBoson     = sample(name="DiBoson",   legendName="VV",                color=kYellow,          lineStyle=1,    markerStyle=26)
diBoson.treeName = "Trees"+channel+"/NJets_noSyst"
Zll         = sample(name="Zll",       legendName="Z/#gamma*#rightarrowl^{+}l^{-}",   color=kOrange-4,    lineStyle=1,    markerStyle=27)
Zll.treeName = "Trees"+channel+"/NJets_noSyst"
fake        = sample(name="Fake",      legendName="QCD",               color=kMagenta+2,       lineStyle=1,    markerStyle=28)
fake.treeName = "Trees"+channel+"/NJets_noSyst"

Wt.inFile       = inputFilePath+"/"+"tW_"+channel+"_noSyst.root"
tchannel.inFile = inputFilePath+"/"+"allTChannel_"+channel+"_noSyst.root"
schannel.inFile = inputFilePath+"/"+"allSChannel_"+channel+"_noSyst.root"
ttbar.inFile    = inputFilePath+"/"+"TTBarMadGraph_"+channel+"_noSyst.root"
wjets.inFile    = inputFilePath+"/"+"WJets_"+channel+"_noSyst.root"
diBoson.inFile  = inputFilePath+"/"+"diBoson_"+channel+"_noSyst.root"
Zll.inFile      = inputFilePath+"/"+"ZJets_"+channel+"_noSyst.root"
fake.inFile     = inputFilePath+"/"+"QCD_"+channel+"_noSyst.root"

stackSampleList.append(Wt);         totalSampleList.append(Wt)
stackSampleList.append(tchannel);   totalSampleList.append(tchannel)
stackSampleList.append(schannel);   totalSampleList.append(schannel)
stackSampleList.append(ttbar);      totalSampleList.append(ttbar)
stackSampleList.append(wjets);      totalSampleList.append(wjets)
stackSampleList.append(diBoson);    totalSampleList.append(diBoson)
stackSampleList.append(Zll);        totalSampleList.append(Zll)
stackSampleList.append(fake);       totalSampleList.append(fake)

sysSampleArray["nominal"] = stackSampleList

########################### prepare the yield information

#getYield(totalSampleList,MCselOpt,dataSelOpt)
#sysList = ['jesup','jesdown','eesup','eesdown']
#for isys in sysList:
#    sysSampleArray.append(isys:sample(name="Wt_"+isys,        legendName="Wt_"+isys,             color=kAzure-3,     lineStyle=1,    markerStyle=21))
#    sysSampleArray.append(isys:sample(name="ttbar_"+isys,     legendName="t\\bar{t}_"+isys,      color=kRed+2,       lineStyle=1,    markerStyle=22))
#    sysSampleArray.append(isys:sample(name="DiBoson_"+isys,   legendName="DiBoson_"+isys,        color=kYellow,      lineStyle=1,    markerStyle=23))
#    sysSampleArray.append(isys:sample(name="Zll_"+isys,       legendName="Zll_"+isys,            color=kOrange-4,    lineStyle=1,    markerStyle=24))
#    sysSampleArray.append(isys:sample(name="Ztautau_"+isys,   legendName="Z\\tau\\tau_"+isys,    color=kOrange+1,    lineStyle=1,    markerStyle=25))
#    sysSampleArray.append(isys:sample(name="Fake_"+isys,      legendName="Fake dilepton_"+isys,  color=kMagenta+2,   lineStyle=1,    markerStyle=26))
#    
#    sysSampleArray[isys][0].inFile = inputFilePath+"/"+"SingleTop.WtDiAcerMCHW"+tag+"MC."+channel+"1+j."+isys+".WtDilepton.rootskimBDT.root"
#    sysSampleArray[isys][1].inFile = inputFilePath+"/"+"SingleTop.ttMCNLO"+tag+"MC."+channel+"1+j."+isys+".WtDilepton.rootskimBDT.root"
#    sysSampleArray[isys][2].inFile = inputFilePath+"/"+"SingleTop.diBoson"+tag+"MC."+channel+"1+j."+isys+".WtDilepton.rootskimBDT.root"
#    sysSampleArray[isys][3].inFile = inputFilePath+"/"+"SingleTop.Zll"+tag+"MC."+channel+"1+j."+isys+".WtDilepton.rootskimBDT.root"
#    sysSampleArray[isys][4].inFile = inputFilePath+"/"+"SingleTop.Ztautau"+tag+"MC."+channel+"1+j."+isys+".WtDilepton.rootskimBDT.root"
#    sysSampleArray[isys][5].inFile = inputFilePath+"/"+"SingleTop.Wjets"+tag+"MC."+channel+"1+j.noshift.WtDilepton.rootskimBDT.root" ## data driven



