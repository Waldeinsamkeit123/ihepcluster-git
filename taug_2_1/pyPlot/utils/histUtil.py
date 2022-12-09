#!/usr/bin/env python
###########################################
###  Tools to handle histograms
###
###  Author: Huaqiao ZHANG  
###  First version: Apr. 2013 @ MSU
###  Contact: huaqiao.zhang@cern.ch
###########################################
#   def hist2AsymmErr(h1):
###########################################
import os
import sys
currentPath = os.getcwd()
sys.path.append( currentPath +"/../"+"utils")
sys.path.append( currentPath +"/../"+"settings")
from ROOT import *
def hist2AsymmErr(h1):
    npoint = h1.GetNbinsX();
    x = []; y =[]; errx_low = []; errx_high = []; erry_low = []; erry_high = []
    for i in range(npoint):
        x.append(h1.GetBinCenter(i+1));
        errx_low.append(h1.GetBinWidth(i+1)/2.);
        errx_high.append(h1.GetBinWidth(i+1)/2.);

        y.append(h1.GetBinContent(i+1));
        erry_low.append(h1.GetBinError(i+1));
        erry_high.append(h1.GetBinError(i+1));
    print (type(x), type(y))
    print (x, y)
    asyErr = TGraphAsymmErrors(npoint,x,y,errx_low,errx_high,erry_low,erry_high);
    return asyErr;


def getEntries(hist, xmin, xmax):
  nbins  = hist.GetNbinsX();
  minBin = hist.FindBin( xmin+1e-10 );
  maxBin = 0;
  if xmin>=xmax:
      maxBin = nbins
  else:
      maxBin = hist.FindBin( xmax-1e-10 )
  
  return hist.Integral(minBin,maxBin)

def SetHistColor(hist, styleName=''):
    if styleName=='':
        print ("Set default style")
    elif styleName=="tW":
        hist.SetLineColor()

if __name__ == '__main__':
    infilename = "../../pyTemplate/testOut.root"
    infile  = TFile(infilename)
    #allhist = infile.GetListOfKeys()
    hist    = infile.Get("ee1j_Wt_HT_nominal")
    nevents = getEntries(hist, 100, 150)
    print (nevents)
    #assyErr = hist2AsymmErr(hist)
    #print assyErr

