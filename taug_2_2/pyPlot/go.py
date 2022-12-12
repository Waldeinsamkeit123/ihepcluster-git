#!/usr/bin/env python
#########################################
### examples to use the plotting tool 
###
###  Author: Huaqiao ZHANG  
###  First version: Apr. 2013 @ MSU
###  Contact: huaqiao.zhang@cern.ch
#########################################
# Function
#   1: stack plot of all background components
#   2: stack plot of all background components compared with data
#   3: stack plot of all background components compared with data + ratio plot at bottom
#   4: compare variable shape 
#   5: compare variable shape + ratio plot at bottom
#   6: compare variable shape and acceptance
#   7: compare variable shape and acceptance + ratio plot at bottom
#########################################
import sys
import os
currentPath = os.getcwd()
sys.path.append( currentPath +"/"+"utils")
sys.path.append( currentPath +"/"+"settings")
from ROOT import *
#import ROOT
gROOT.LoadMacro(currentPath+"/styles/AtlasStyle.C") 
##########################################################################################
from inputUtil import *       ### common tools to handle input files
from plotUtil import *        ### common tools to handle plots
from histUtil import *        ### common tools to handle histograms
##########################################################################################
#############  User defined file:  input File, plotting variables, selection criteria
from inputFile import *      #### define stackSampleList and dataSampleList
from plotVariable import *   #### define plotList
from selectionCut import *   #### define MCselOpt and dataSelOpt
##########################################################################################

c1      = TCanvas("c1","c1",800,600)

for ivar in range(len(plotList)):
    histList,rooFile = getHistFromTree(stackSampleList,plotList[ivar],MCselOpt,dataSelOpt)
    #for ihist in range(len(histList)):
    #	print histList[ihist].GetTitle()
    histNameList = getLegendNameList(stackSampleList)
    #print histNameList

    dataList,rooFile2 = getHistFromTree(dataSampleList,plotList[ivar],MCselOpt,dataSelOpt)
    dataNameList = getLegendNameList(dataSampleList)

    addUnderFlowAndOverFlow(histList+dataList)
    plotCTR = plotsSetting()  ### plots setting class that include all the setting information
    plotCTR.m_logy = 0

####### 1: stack plot only
#    plotCTR.autoSetLegend(histList+dataList,"FullSize")
#    plotCTR.autoSetYaxisRange(dataList+[addHist(histList)])
#    legend  = plotCTR.stackPlot(c1,histList,histNameList)
##########################

######## 2: compare stack and data without ratio
#    plotCTR.autoSetLegend(histList+dataList,"FullSize")
#    plotCTR.autoSetYaxisRange(dataList+[addHist(histList)])
#    legend,vec,total = plotCTR.stackPlotCompareData(c1,histList,histNameList,dataList,dataNameList)
##########################

####### 3: compare stack and data with ratio plot at bottom
    plotCTR.autoSetLegend(histList+dataList,"upperSize")
    plotCTR.autoSetYaxisRange(dataList+[addHist(histList)])
    legend,vec,total = plotCTR.stackPlotCompareDataWithRatio(c1,histList,histNameList,dataList,dataNameList)
#########################

####### 4: compare shape only without ratio
#    normalizeHist(histList)
#    plotCTR.autoSetLegend(histList,"FullSize")
#    plotCTR.autoSetYaxisRange(histList)
#    legend  = plotCTR.compareShapeAndNorm(c1,histList,histNameList)
#########################

####### 5: compare shape only with ratio plots at bottom
#    normalizeHist(histList)
#    plotCTR.autoSetLegend(histList,"upperSize")
#    plotCTR.autoSetYaxisRange(histList)
#    legend  = plotCTR.compareShapeAndNormWithRatio(c1,histList,histNameList)
#########################

####### 6: compare shape and acceptance without ratio
#    plotCTR.autoSetLegend(histList,"FullSize")
#    plotCTR.autoSetYaxisRange(histList)
#    legend  = plotCTR.compareShapeAndNorm(c1,histList,histNameList)
########################

####### 7: compare shape and acceptance with ratio plot at bottom
#    plotCTR.autoSetLegend(histList,"upperSize")
#    plotCTR.autoSetYaxisRange(histList)
#    plotCTR.m_ratioYaxisMax = 3
#    plotCTR.m_ratioYaxisMin = -0.1
#    legend  = plotCTR.compareShapeAndNormWithRatio(c1,histList,histNameList)
########################

    c1.Update()
    c1.SaveAs("plots/test_"+plotList[ivar].varName+".gif")
    c1.Clear()



