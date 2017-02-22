# generic imports 

import ROOT as rt
import numpy as np
import math
import matplotlib.pyplot as plt
import seaborn
from rootpy.plotting import Hist, HistStack, Graph, Canvas, Legend
from rootpy.plotting.style import get_style, set_style
from rootpy.interactive import wait
from rootpy.plotting.utils import draw
import rootpy.plotting.root2matplotlib as rplt
from glob import glob 



# self-written code imports

from parser_constants import * # get constants used in this file

# extract necessary functions from helper/analysis code
from fillhists import *
from calculate import *


'''

extract_JetPT(f_tt, f_qcd, f_wjet)

This is the general function dealing with Jet.PT data. Get trees from files and 
create histograms. Fill necessary trees, and create plots.

'''
   
def do_analysis(chain, analyze_this, outfile, eventtype):
    
    # get trees from files
    #t = f.Get("Delphes")
    
    # get number of entries
    nentries = chain.GetEntries()
    
    # initialize everything here before filling histograms
    
    if (analyze_this['Jet.PT']):
        print "\nInitializing Jet.PT...\n"
        
        # create the histograms
        numJets = Hist(NBINS,NLO,NHI, title = 'numJets ' + eventtype, legendstyle = 'L')

        # interesting values to plot
        max_jetpt_per_event = Hist(PT_NBINS,PT_NLO,PT_NHI, title = 'Max JetPT/Event ' + eventtype, legendstyle = 'L')
        min_jetpt_per_event = Hist(PT_NBINS,PT_NLO,PT_NHI, title = 'Min JetPT/Event ' + eventtype, legendstyle = 'L')

    else:
        print "Skipped Jet.PT"
        
        
    if (analyze_this['Jet.BTag']):
        print "Initializing Jet.BTag...\n"
               
        # create the histograms
        loose = Hist(NBINS,NLO,NHI, title = 'loose ' + eventtype, legendstyle = 'L')
        medium = Hist(NBINS,NLO,NHI, title = 'medium ' + eventtype, legendstyle = 'L')
        tight = Hist(NBINS,NLO,NHI, title = 'tight ' + eventtype, legendstyle = 'L')

    else:
        print "Skipped Jet.BTag"
        
        
    if (analyze_this['Electron.PT']):
        print "Initializing Electron.PT...\n"
                
        # create the histograms
        numElectrons = Hist(NBINS,NLO,NHI, title = 'numElectrons ' + eventtype, legendstyle = 'L')

        # interesting values to plot
        max_ept_per_event = Hist(PT_NBINS,PT_NLO,PT_NHI, title = 'Max ElectronPT/Event ' + eventtype, legendstyle = 'L')
        min_ept_per_event = Hist(PT_NBINS,PT_NLO,PT_NHI, title = 'Min ElectronPT/Event ' + eventtype, legendstyle = 'L')
        
        # initialize any variable-specific constants here:
        
        # counter for no electrons
        noeleaf = 0

    else:
        print "Skipped Electron.PT" 
    
        
        
    if (analyze_this['MuonTight.PT']):
        print "Initializing MuonTight.PT...\n"
        
        
        # create the histograms
        numMuons = Hist(NBINS,NLO,NHI, title = 'numMuons ' + eventtype, legendstyle = 'L')

        # interesting values to plot
        max_upt_per_event = Hist(PT_NBINS,PT_NLO,PT_NHI, title = 'Max MuonPT/Event ' + eventtype, legendstyle = 'L')
        min_upt_per_event = Hist(PT_NBINS,PT_NLO,PT_NHI, title = 'Min MuonPT/Event ' + eventtype, legendstyle = 'L')

        # initialize any variable-specific constants here:
        
        # counter for no electrons
        nouleaf = 0

    else:
        print "Skipped MuonTight.PT"     
        
        
    if (analyze_this['MissingET.MET']):
        print "Initializing MissingET.MET...\n"
        
        # create the histograms
        MET = Hist(MET_NBINS, MET_NLO, MET_NHI, title = 'MET ' + eventtype, legendstyle = 'L')
        
    else:
        print "Skipped MissingET.MET" 
        
        
    if (analyze_this['MT (NON-LEAF)']):
        print "Initializing MT...\n"   
        
        # create the histograms
        MT = Hist(MT_NBINS, MT_NLO, MT_NHI, title = 'MT ' + eventtype, legendstyle = 'L')
        
    else:
        print "Skipped HT"
        
    if (analyze_this['HT (NON-LEAF)']):
        print "Initializing HT...\n"   
        
        # create the histograms
        HT = Hist(HT_NBINS, HT_NLO, HT_NHI, title = 'HT ' + eventtype, legendstyle = 'L')
        
    else:
        print "Skipped HT"
        
    
    if (analyze_this['DELTA PHI (NON-LEAF)']):
        print "Initializing Delta Phi...\n"   
        
        # create the histograms
        DPHI = Hist(30, -1*np.pi, np.pi, title = 'Delta Phi ' + eventtype, legendstyle = 'L')
        
    else:
        print "Skipped HT"    
       
        
        
        
        
    
    # Now fill histograms
    
    print "\nFilling histograms...\n"
    
    # get float version of num entries to normalize below; subtract 1 to get 
    # actual integral value of hist
    norm = float(nentries - 1)
    
    
    for e in range(nentries):
        
        entry = chain.GetEntry(e)
        
        # to check whether each entry is electron or muon
        is_electron = False
        is_muon = False
        
        e_maxpt = 0
        e_maxpt_phi = 0
        
        u_maxpt = 0
        u_maxpt_phi = 0
        
        if (analyze_this['Jet.PT']):
        
            # define leaves       
            var = 'Jet.PT'
            
            leaf = chain.GetLeaf(var)
            
            # analyze with Jet.PT because HT is sum of Jet.PTs
            if (analyze_this['HT (NON-LEAF)']):
                HTfill = True
            else:
                HTfill = False
            
            fill_JetPT_hist(chain, leaf, entry, numJets, min_jetpt_per_event, max_jetpt_per_event, HTfill, HT)
            
            
        
        if (analyze_this['Jet.BTag']):
        
            # define leaves
            var = "Jet.BTag"
            
            leaf = chain.GetLeaf(var)
        
            fill_JetBTag_hist(chain, leaf, entry, loose, medium, tight)    
            
            
        if (analyze_this['Electron.PT']):
            
            
            # define leaves
            var = "Electron.PT"
            
            leaf = chain.GetLeaf(var)
            phileaf = chain.GetLeaf('Electron.Phi')
            
            
            # returns phi of max pt for entry
            (e_maxpt, e_maxpt_phi) = fill_Electron_hist(chain, leaf, entry, numElectrons, min_ept_per_event, max_ept_per_event, phileaf)
            
            if (leaf.GetLen() == 0):
                noeleaf += 1
                e_maxpt = 0
                e_maxpt_phi = 0
            else:
                is_electron = True
                
                
    
        if (analyze_this['MuonTight.PT']):
            
            # define leaves
            var = "MuonTight.PT"
            
            leaf = chain.GetLeaf(var)
            phileaf = chain.GetLeaf('MuonTight.Phi')
            
            
            (u_maxpt, u_maxpt_phi) = fill_Muon_hist(chain, leaf, entry, numMuons, min_upt_per_event, max_upt_per_event, phileaf)
            
            if leaf.GetLen() == 0:
                nouleaf += 1
                u_maxpt = 0
                u_maxpt_phi = 0
            else:
                is_muon = True
                
    
        if (analyze_this['MissingET.MET']):
        
            # define leaves
            var = "MissingET.MET"
            
            leaf = chain.GetLeaf(var)    
            phileaf = chain.GetLeaf('MissingET.Phi')        
            
            (met, metphi) = fill_MET_hist(chain, leaf, entry, MET, phileaf)   
         
        if (analyze_this['MT (NON-LEAF)']):
            #print "ok got here"
            #print "here ",e_maxpt, e_maxpt_phi, u_maxpt, u_maxpt_phi, met, metphi
            
            mt_val = get_mt(e_maxpt, e_maxpt_phi, u_maxpt, u_maxpt_phi, met, metphi)
            if mt_val == 0:
                MT.Fill(INVALID)
            else:
                MT.Fill(mt_val)
            
        if (analyze_this['DELTA PHI (NON-LEAF)']):
            
            if e_maxpt > u_maxpt:
                lphi = e_maxpt_phi
            else:
                lphi = u_maxpt_phi
            
            dphival = delta_phi(metphi, lphi)
            #dphi_MET-jet(metphi, 
            #print dphival
            DPHI.Fill(dphival)
            
    
    
    

    if (analyze_this['Jet.PT']):

        # normalize
        numJets.Scale(1/norm)
        max_jetpt_per_event.Scale(1/norm)
        min_jetpt_per_event.Scale(1/norm)
    
    if (analyze_this['Jet.BTag']):
   
        # normalize
        tight.Scale(1/norm)
        medium.Scale(1/norm)
        loose.Scale(1/norm) 
        
    if (analyze_this['Electron.PT']):        
                
        # normalize
        numElectrons.Scale(1/norm)
        max_ept_per_event.Scale(1/norm)
        min_ept_per_event.Scale(1/norm)
        
        print "\nentries: " + str(nentries) + " noeleaf number: " + str(noeleaf) 
        
    if (analyze_this['MuonTight.PT']):        
                
        # normalize
        numMuons.Scale(1/norm)
        max_upt_per_event.Scale(1/norm)
        min_upt_per_event.Scale(1/norm)
        
        print "\nentries: " + str(nentries) + " nouleaf number: " + str(nouleaf) 

    if (analyze_this['MissingET.MET']):
   
        # normalize
        MET.Scale(1/norm)
        
    if (analyze_this['MT (NON-LEAF)']):
        
        #normalize
        MT.Scale(1/norm)

    if (analyze_this['HT (NON-LEAF)']):
        
        #normalize
        HT.Scale(1/norm)
        
    if (analyze_this['DELTA PHI (NON-LEAF)']):
        
        #normalize
        DPHI.Scale(1/norm)

    print ""
    print "\nDone!\n"

    






    
    
    numJets.Write(eventtype + "numJets")
    max_jetpt_per_event.Write(eventtype + "max_jetpt_per_event")
    min_jetpt_per_event.Write(eventtype + "min_jetpt_per_event")
    
    loose.Write(eventtype + "loose")
    medium.Write(eventtype + "medium")
    tight.Write(eventtype + "tight")   
    
    numElectrons.Write(eventtype + "numElectrons")
    max_ept_per_event.Write(eventtype + "max_ept_per_event")
    min_ept_per_event.Write(eventtype + "min_ept_per_event")
    
    numMuons.Write(eventtype + "numMuons")
    max_upt_per_event.Write(eventtype + "max_upt_per_event")
    min_upt_per_event.Write(eventtype + "min_upt_per_event")
    
    MET.Write(eventtype + "MET")
    
    MT.Write(eventtype + "MT")
    
    HT.Write(eventtype + "HT")
    
    DPHI.Write(eventtype + "dphi")
    
    


   
def main():
    
      
    
    # array of stuff needed to be analyzed
    # NON-LEAF refers to internal analysis from other leaves
    want_leaves = ['Jet.PT', 'Jet.BTag', 'Electron.PT', 'MuonTight.PT', 'MuonTight.Phi', 'MissingET.MET', 'MT (NON-LEAF)', 'HT (NON-LEAF)', 'DELTA PHI (NON-LEAF)']
    
    # bits to be set if want analyzed:
    # Jet.PT = 0 (rightmost binary bit)
    # Jet.BTag = 1
    # Electron.PT = 2
    # MuonTight.PT = 3
    # MissingET.MET = 4 (leftmost binary bit)
    
    
    
    # print out leaves used in analysis for user
    print "\nDefault analysis includes: \n" + "\n".join(want_leaves)
    
    while True:
        
        # Determine which files to analyze
        
        # if want all analyses done. Or statement ensures there is a default value
        if (int(raw_input("\nPress 'Enter' if default analysis okay or '0' to " + 
        "skip: ") or '1')):
        
            # default to do all analysis (set everything)
            leaf_bits = [1] * len(want_leaves) 
            
        # only want to do specific analyses    
        else:
            print ("\nPress 'Enter' if each analysis is ok, or '0' to skip")
            print ""
            
            leaf_bits = []
            
            # ask if want to analyze each leaf in want_leaves list
            for i in want_leaves:
                leaf_bits.append(int(raw_input("{} analysis: ".format(i)) or '1'))
                
            print ""
            
        
        # create dictionary associating set bits to possible leafs
        analyze_this = dict(zip(want_leaves, leaf_bits))
        print "\nFinal dictionary: ", (analyze_this)
        
        # make sure user likes the analysis choices, otherwise reloop through
        # all options again
        if(int(raw_input("\nIs this dictionary okay? " +
        "Press 'Enter' if yes, or '0' if no: ") or '1')):
            break
        
    print ""
    
    newf = rt.TFile("chainedhists.root", "recreate")
    
    alleventtypes = ['tt', 'qcd', 'wjet']
      
    # get default debugging files    
    ttfiles = glob('../../../ttbar_data/ttbar/ttbar*.root')
    qcdfiles = glob('../../../ttbar_data/ttbar/qcd*.root')
    wjetfiles = glob('../../../ttbar_data/ttbar/wjet*.root')
    
    allfiles = [ttfiles, qcdfiles, wjetfiles]
    
    
    cntr = 0
    
    for i in allfiles:
        chain = rt.TChain('Delphes')
        eventtype = alleventtypes[cntr]
        print "\nChaining and analyzing " + eventtype + "...\n"        
        
        for f in i:
            chain.Add(f)
        
        do_analysis(chain, analyze_this, newf, eventtype)
        cntr = cntr + 1
        
    newf.Close()         



if __name__ == "__main__":
    main();
    
    
    
    
    
    
    
    
