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
   
def do_analysis(f, eventtype, analyze_this):
    
    # get trees from files
    t = f.Get("Delphes")
    
    # get number of entries
    nentries = t.GetEntries()
    
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
        print "Skipped MT"
        
        
        
        
        
        
        
    
    # Now fill histograms
    
    print "\nFilling histograms...\n"
    
    # get float version of num entries to normalize below; subtract 1 to get 
    # actual integral value of hist
    norm = float(nentries - 1)
    
    
    for e in range(nentries):
        
        entry = t.GetEntry(e)
        
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
            
            leaf = t.GetLeaf(var)
            
            fill_JetPT_hist(t, leaf, entry, numJets, min_jetpt_per_event, max_jetpt_per_event)
        
        if (analyze_this['Jet.BTag']):
        
            # define leaves
            var = "Jet.BTag"
            
            leaf = t.GetLeaf(var)
        
            fill_JetBTag_hist(t, leaf, entry, loose, medium, tight)    
            
            
        if (analyze_this['Electron.PT']):
            
            
            # define leaves
            var = "Electron.PT"
            
            leaf = t.GetLeaf(var)
            phileaf = t.GetLeaf('Electron.Phi')
            
            
            # returns phi of max pt for entry
            (e_maxpt, e_maxpt_phi) = fill_Electron_hist(t, leaf, entry, numElectrons, min_ept_per_event, max_ept_per_event, phileaf)
            
            if (leaf.GetLen() == 0):
                noeleaf += 1
                e_maxpt = 0
                e_maxpt_phi = 0
            else:
                is_electron = True
                
                
    
        if (analyze_this['MuonTight.PT']):
            
            # define leaves
            var = "MuonTight.PT"
            
            leaf = t.GetLeaf(var)
            phileaf = t.GetLeaf('MuonTight.Phi')
            
            
            (u_maxpt, u_maxpt_phi) = fill_Muon_hist(t, leaf, entry, numMuons, min_upt_per_event, max_upt_per_event, phileaf)
            
            if leaf.GetLen() == 0:
                nouleaf += 1
                u_maxpt = 0
                u_maxpt_phi = 0
            else:
                is_muon = True
                
    
    
        if (analyze_this['MissingET.MET']):
        
            # define leaves
            var = "MissingET.MET"
            
            leaf = t.GetLeaf(var)    
            phileaf = t.GetLeaf('MissingET.Phi')        
            
            (met, metphi) = fill_MET_hist(t, leaf, entry, MET, phileaf)   
         
        if (analyze_this['MT (NON-LEAF)']):
            #print "ok got here"
            #print "here ",e_maxpt, e_maxpt_phi, u_maxpt, u_maxpt_phi, met, metphi
            
            mt_val = get_mt(e_maxpt, e_maxpt_phi, u_maxpt, u_maxpt_phi, met, metphi)
            if mt_val == 0:
                MT.Fill(INVALID)
            else:
                MT.Fill(mt_val)
            
            #print mt_val
    
    
    
    

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

    print ""
    print "\nDone!\n"








    # write to TFiles
    newf = rt.TFile(eventtype + "hists.root", "recreate")
    
    numJets.Write("numJets")
    max_jetpt_per_event.Write("max_jetpt_per_event")
    min_jetpt_per_event.Write("min_jetpt_per_event")
    
    loose.Write("loose")
    medium.Write("medium")
    tight.Write("tight")   
    
    numElectrons.Write("numElectrons")
    max_ept_per_event.Write("max_ept_per_event")
    min_ept_per_event.Write("min_ept_per_event")
    
    numMuons.Write("numMuons")
    max_upt_per_event.Write("max_upt_per_event")
    min_upt_per_event.Write("min_upt_per_event")
    
    MET.Write("MET")
    
    MT.Write("MT")
    
    newf.Close()


   
def main():

    # get files 
    f_tt = rt.TFile("../../../ttbar_data/ttbar_lepFilter_13TeV_313.root")
    f_qcd = rt.TFile("../../../ttbar_data/qcd_lepFilter_13TeV_10.root")
    f_wjet = rt.TFile("../../../ttbar_data/wjets_lepFilter_13TeV_3.root")
    
    # array of stuff needed to be analyzed
    # NON-LEAF refers to internal analysis from other leaves
    want_leaves = ['Jet.PT', 'Jet.BTag', 'Electron.PT', 'MuonTight.PT', 'MuonTight.Phi', 'MissingET.MET', 'MT (NON-LEAF)']
    
    # bits to be set if want analyzed:
    # Jet.PT = 0 (rightmost binary bit)
    # Jet.BTag = 1
    # Electron.PT = 2
    # MuonTight.PT = 3
    # MissingET.MET = 4 (leftmost binary bit)
    
    
    
    # print out leaves used in analysis for user
    print "\nDefault analysis includes: \n" + "\n".join(want_leaves)
    
    while True:
        
        # if want all analyses done. Or statement ensures there is a default value
        if (int(raw_input("\nPress 'Enter' if default analysis okay or '0' or " + 
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
    
    # run functions you want here
    do_analysis(f_qcd, 'qcd', analyze_this)
                 

if __name__ == "__main__":
    main();
    
    
    
    
    
    
    
    
