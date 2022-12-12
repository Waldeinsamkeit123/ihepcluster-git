#!/usr/bin/env python
#########################################
### place to define the final selection 
###
###  Author: Huaqiao ZHANG  
###  First version: Apr. 2013 @ MSU
###  Contact: huaqiao.zhang@cern.ch
#########################################
# Data member:
#   dataSelOpt
#   MCselOpt
#########################################
import os
import sys
currentPath = os.getcwd()
sys.path.append( currentPath +"/../"+"utils")
sys.path.append( currentPath +"/../"+"settings")
from ROOT import *
########################### common block #############################
commonSel = "Event.Nparticles>0"

dataSelOpt = commonSel

MCselOpt = commonSel

#######################################################################

