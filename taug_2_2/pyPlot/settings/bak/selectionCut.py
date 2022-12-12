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
commonSel = "(((DeltaPhiLeadingLeptonMissingEt+DeltaPhiSubLeadingLeptonMissingEt)>2.5&&(!(((LeadingLeptonPhi>-0.74&&LeadingLeptonPhi<-0.64&&LeadingLeptonEta>0.1&&LeadingLeptonEta<1.4)||(SubLeadingLeptonPhi>-0.74&&SubLeadingLeptonPhi<-0.64&&SubLeadingLeptonEta>0.1&&SubLeadingLeptonEta<1.4)||(Jet1Phi>-0.84&&Jet1Phi<-0.54&&Jet1Eta>0.0&&Jet1Eta<1.5)||(Jet2Phi>-0.84&&Jet2Phi<-0.54&&Jet2Eta>0.0&&Jet2Eta<1.5)||(Jet3Phi>-0.84&&Jet3Phi<-0.54&&Jet3Eta>0.0&&Jet3Eta<1.5)||(Jet4Phi>-0.84&&Jet4Phi<-0.54&&Jet4Eta>0.0&&Jet4Eta<1.5))&&RunNumber>180613))))*((NJets==1)||(NJets>=2&&Jet2Pt<30))"

dataSelOpt = commonSel

MCselOpt = "20.5*EventWeight*PileupWeight*"+commonSel

#######################################################################

