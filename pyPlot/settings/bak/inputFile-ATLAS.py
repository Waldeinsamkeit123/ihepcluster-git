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
tag = 'LP2fb_fake'
channel = 'em'
inputFilePath = "/Users/huaqiao/work/anaPackage/macros/mergRootOutFile/"+tag

data2011    = sample(name="data2011",   color=kBlack,       lineStyle=1,    markerStyle=20)
data2011.inFile = inputFilePath+"/"+"SingleTop.data2011"+tag+"Data."+channel+"1+j.noshift.WtDilepton.rootskimBDT.root"
data2011.dataType = "data"
dataSampleList.append(data2011);   totalSampleList.append(data2011)

Wt          = sample(name="Wt",        legendName="Wt",         color=kAzure-3,     lineStyle=1,    markerStyle=21)
ttbar       = sample(name="ttbar",     legendName="t\\bar{t}",  color=kRed+2,       lineStyle=1,    markerStyle=22)
diBoson     = sample(name="DiBoson",   legendName="DiBoson",    color=kYellow,      lineStyle=1,    markerStyle=23)
Zll         = sample(name="Zll",       legendName="Zll",        color=kOrange-4,    lineStyle=1,    markerStyle=24)
Ztautau     = sample(name="Ztautau",   legendName="Ztautau",    color=kOrange+1,    lineStyle=1,    markerStyle=25)
fake        = sample(name="Fake",      legendName="fake",       color=kMagenta+2,   lineStyle=1,    markerStyle=26)

Wt.inFile       = inputFilePath+"/"+"SingleTop.WtDiAcerMCHW"+tag+"MC."+channel+"1+j.noshift.WtDilepton.rootskimBDT.root"
ttbar.inFile    = inputFilePath+"/"+"SingleTop.ttMCNLO"+tag+"MC."+channel+"1+j.noshift.WtDilepton.rootskimBDT.root"
diBoson.inFile  = inputFilePath+"/"+"SingleTop.diBoson"+tag+"MC."+channel+"1+j.noshift.WtDilepton.rootskimBDT.root"
Zll.inFile      = inputFilePath+"/"+"SingleTop.Zll"+tag+"MC."+channel+"1+j.noshift.WtDilepton.rootskimBDT.root"
Ztautau.inFile  = inputFilePath+"/"+"SingleTop.Ztautau"+tag+"MC."+channel+"1+j.noshift.WtDilepton.rootskimBDT.root"
fake.inFile     = inputFilePath+"/"+"SingleTop.Wjets"+tag+"MC."+channel+"1+j.noshift.WtDilepton.rootskimBDT.root"

stackSampleList.append(Wt);         totalSampleList.append(Wt)
stackSampleList.append(ttbar);      totalSampleList.append(ttbar)
stackSampleList.append(diBoson);    totalSampleList.append(diBoson)
stackSampleList.append(Zll);        totalSampleList.append(Zll)
stackSampleList.append(Ztautau);    totalSampleList.append(Ztautau)
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



