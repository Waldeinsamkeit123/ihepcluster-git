from ROOT import *
from math import *
def optmizeLowerThreshold(icut,histSIG,histBKG,isysHistList,isysPairList,isysTheoryPairList,isysTheoryPairSymetrizeList,minBin,maxBin):
    signal = histSIG.Integral(icut,maxBin)
    bkgd   = histBKG.Integral(icut,maxBin)

    statBKG2 = 0
    for ibin in range(icut,maxBin):
        statBKG2 = statBKG2 + pow(histBKG.GetBinError(ibin),2)
    deltaBKG2 = statBKG2   ## include the statistical error
    
    for isysHist in isysHistList:
        deltaBKG2 = deltaBKG2 + pow(isysHist[0].Integral(icut,maxBin)-bkgd,2)  ### include symmetrized systematics error
    for isysPair in isysPairList:
        #print isysPair[0]
        #print isysPair[0][0]
        updelta = isysPair[0][0].Integral(icut,maxBin)-bkgd
        downdelta = isysPair[1][0].Integral(icut,maxBin)-bkgd
        #print updelta/bkgd,downdelta/bkgd
        deltaBKG2 = deltaBKG2 + pow( (fabs(updelta)+fabs(downdelta))/2., 2)  ### include paired systematics error
    for isysPair in isysTheoryPairList:
        deltaBKG2 = deltaBKG2 + pow( (isysPair[0][0].Integral(icut,maxBin)-isysPair[1][0].Integral(icut,maxBin))/2., 2)  ### include paired ISRFSR systematics error
    for isysThPair in isysTheoryPairSymetrizeList:
        if isysThPair[0][0].Integral(icut,maxBin)!=0 and bkgd!=0:
            delta = bkgd * (isysThPair[1][0].Integral(icut,maxBin)-isysThPair[0][0].Integral(icut,maxBin))/isysThPair[0][0].Integral(icut,maxBin) 
        else: 
            delta = isysThPair[1][0].Integral(icut,maxBin)-isysThPair[0][0].Integral(icut,maxBin)
        deltaBKG2 = deltaBKG2 + pow( delta, 2)  ### include paired parton shower/generator systematics error
    
    deltaBKG = sqrt(deltaBKG2)
    pbi=0;zbi=0; 
    if deltaBKG == 0:
        #print "icut = ", icut, "delta BKG = 0, set zbi to 0"
        zbi = 0
    else:
        tau  = bkgd/(deltaBKG*deltaBKG)
        noff = tau*bkgd;
        non  = signal + bkgd; ## total events in region after cut 
        pbi  = TMath.BetaIncomplete(1. / (1. + tau), non, noff + 1);
        zbi  = sqrt(2.) * TMath.ErfInverse(1-2*pbi)  
    if zbi<0:
        #print "icut = ",icut, "zbi < 0, set zbi to 0"
        zbi=0
    #print icut, signal, bkgd, tau, noff, non, pbi, zbi
    if pbi<=0:
        mlogpbi = 0
    else:
        mlogpbi = -log(pbi)
    statSig = -1
    if bkgd>0:
        statSig = signal/sqrt(bkgd)
    return  mlogpbi,zbi,statSig

def optmizeUpperThreshold(icut,histSIG,histBKG,isysHistList,isysPairList,isysTheoryPairList,isysTheoryPairSymetrizeList,minBin,maxBin):
    signal = histSIG.Integral(minBin,icut)
    bkgd   = histBKG.Integral(minBin,icut)

    statBKG2 = 0
    for ibin in range(minBin,icut):
        statBKG2 = statBKG2 + pow(histBKG.GetBinError(ibin),2)
    deltaBKG2 = statBKG2   ## include the statistical error
    
    for isysHist in isysHistList:
        deltaBKG2 = deltaBKG2 + pow(isysHist[0].Integral(minBin,icut)-bkgd,2)  ### include symmetrized systematics error
    for isysPair in isysPairList:
        #print isysPair[0]
        #print isysPair[0][0]
        updelta = isysPair[0][0].Integral(minBin,icut)-bkgd
        downdelta = isysPair[1][0].Integral(minBin,icut)-bkgd
        #print updelta/bkgd,downdelta/bkgd
        deltaBKG2 = deltaBKG2 + pow( (fabs(updelta)+fabs(downdelta))/2., 2)  ### include paired systematics error
    for isysPair in isysTheoryPairList:
        deltaBKG2 = deltaBKG2 + pow( (isysPair[0][0].Integral(minBin,icut)-isysPair[1][0].Integral(minBin,icut))/2., 2)  ### include paired ISRFSR systematics error
    for isysThPair in isysTheoryPairSymetrizeList:
        if isysThPair[0][0].Integral(minBin,icut)!=0 and bkgd!=0:
            delta = bkgd * (isysThPair[1][0].Integral(minBin,icut)-isysThPair[0][0].Integral(minBin,icut))/isysThPair[0][0].Integral(minBin,icut) 
        else: 
            delta = isysThPair[1][0].Integral(minBin,icut)-isysThPair[0][0].Integral(minBin,icut)
        deltaBKG2 = deltaBKG2 + pow( delta, 2)  ### include paired parton shower/generator systematics error
    
    deltaBKG = sqrt(deltaBKG2)
    pbi=0;zbi=0; 
    if deltaBKG == 0:
        #print "icut = ", icut, "delta BKG = 0, set zbi to 0"
        zbi = 0
    else:
        tau  = bkgd/(deltaBKG*deltaBKG)
        noff = tau*bkgd;
        non  = signal + bkgd; ## total events in region after cut 
        pbi  = TMath.BetaIncomplete(1. / (1. + tau), non, noff + 1);
        zbi  = sqrt(2.) * TMath.ErfInverse(1-2*pbi)  
    if zbi<0:
        #print "icut = ",icut, "zbi < 0, set zbi to 0"
        zbi=0
    #print icut, signal, bkgd, tau, noff, non, pbi, zbi
    if pbi<=0:
        mlogpbi = 0
    else:
        mlogpbi = -log(pbi)
    statSig = -1
    if bkgd>0:
        statSig = signal/sqrt(bkgd)
    return  mlogpbi,zbi,statSig

