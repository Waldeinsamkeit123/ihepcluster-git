#!/usr/bin/env python
###########################################
###  Place to define plotting variables
###
###  Author: Huaqiao ZHANG  
###  First version: Apr. 2013 @ MSU
###  Contact: huaqiao.zhang@cern.ch
###########################################
# Data member
#   plotList
###########################################
import os
import sys
currentPath = os.getcwd()
sys.path.append( currentPath +"/../"+"utils")
sys.path.append( currentPath +"/../"+"settings")
from ROOT import *
from inputUtil import *
from plotUtil import *
from inputFile import *

plotList = []
#
HT = treeVarPlot(totalSampleList,varName="HT",xmin=0,xmax=500,scale=1.,nBin=20)
HT.XaxisTitle = "HT [GeV] "; plotList.append(HT)


#

#
