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
PT = treeVarPlot(totalSampleList,varName="Particle.PT",xmin=0,xmax=50,scale=1.,nBin=50)
PT.XaxisTitle = "PT"; plotList.append(PT)

#
Eta = treeVarPlot(totalSampleList,varName="Particle.Eta",xmin=0,xmax=50,scale=1.,nBin=50)
Eta.XaxisTitle = "Eta"; plotList.append(Eta)

#
Phi = treeVarPlot(totalSampleList,varName="Particle.Phi",xmin=0,xmax=50,scale=1.,nBin=50)
Phi.XaxisTitle = "Phi"; plotList.append(Phi)

#
E = treeVarPlot(totalSampleList,varName="Particle.E",xmin=0,xmax=50,scale=1.,nBin=50)
E.XaxisTitle = "E"; plotList.append(E)