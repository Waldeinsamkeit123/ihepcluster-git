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
NParticles = treeVarPlot(totalSampleList,varName="Event.Nparticles",xmin=0,xmax=50,scale=1.,nBin=50)
NParticles.XaxisTitle = "Nparticles "; plotList.append(NParticles)


#

#
