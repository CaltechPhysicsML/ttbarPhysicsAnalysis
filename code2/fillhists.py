# generic imports 

import ROOT as rt
import numpy as np
import matplotlib.pyplot as plt
import seaborn
from rootpy.plotting import Hist, HistStack, Graph, Canvas, Legend
from rootpy.plotting.style import get_style, set_style
from rootpy.interactive import wait
from rootpy.plotting.utils import draw
import rootpy.plotting.root2matplotlib as rplt



# self-written code imports

from parser_constants import * # get constants used in this file
from calculate import min_deltaR_jetlep

'''

fill_JetPT_hist(chain, leaf, numJets, minJet, maxJet)

Fills gives chain over nentries. Iterates through leaf values to extract
numJets, minJet, and maxJet values to fill. Normalizes the numJets, minJet, 
and maxJet histograms.

'''

def fill_JetPT_hist(chain, leaf, entry, numJets, minJet, maxJet, HTfill, HT, phileaf, etaleaf, lepton_vec):
    
    # counter for number of values per entry > JETPT_THRESHOLD
    cntr = 0
    
    # max & min vals, just make initial value
    maxjetpt = INVALID
    minjetpt = INVALID
    
    # summing of PTs in HT
    HT_total = INVALID
    
    # tracker for phi
    maxpt_phi = INVALID
    maxpt_eta = INVALID
    
    #iterate through each value in leaf of jet pts
    for i in range(leaf.GetLen()):
        curr_val = leaf.GetValue(i) # get the value
        curr_phi = phileaf.GetValue(i)
        curr_eta = etaleaf.GetValue(i)
        
        #print "i: %d CURR VAL: %f" % (i, curr_val)
        #print min_deltaR_jetlep(curr_phi, curr_eta, lepton_vec)
        
        if (min_deltaR_jetlep(curr_phi, curr_eta, lepton_vec) > 0.4):
            # only care about values with > JETPT_THRESHOLD
            if ((curr_val > JETPT_THRESHOLD_LO) & (curr_val < JETPT_THRESHOLD_HI)):
                #print "JET PT VAL: %f" % curr_val # to see if in order
                cntr += 1
                
                if ((curr_val > maxjetpt) | (maxjetpt == INVALID)):
                    maxjetpt = curr_val
                    maxpt_phi = curr_phi
                    maxpt_eta = curr_eta
                    
                if ((curr_val < minjetpt) | (minjetpt == INVALID)):
                    minjetpt = curr_val
                    
                if (HTfill):
                    if curr_val > 0:
                        HT_total = HT_total + curr_val
        
    
   #if (minjetpt < 10.0):       
        #print "MIN: %f MAX: %f" % (minjetpt, maxjetpt)
    
    # get number of jets with jetpt > JETPT_THRESHOLD        
    numJets.Fill(cntr) 
    maxJet.Fill(maxjetpt)
    minJet.Fill(minjetpt) 
    
    if (HTfill):
        HT.Fill(HT_total)
    
    return (maxjetpt, maxpt_phi, maxpt_eta)    



'''

fill_JetBTag_hist(nentries, chain, leaf, numJets, minJet, maxJet)

Fills gives chain over nentries given. Iterates through leaf values to extract
numJets, minJet, and maxJet values to fill. Normalizes the numJets, minJet, 
and maxJet histograms.

'''

def fill_JetBTag_hist(chain, leaf, entry, numLoose, numMedium, numTight):

    # counter for number of values per entry > JETPT_THRESHOLD
    cntr_tight = 0
    cntr_medium = 0
    cntr_loose = 0
    
   
    #print "MIN: %f MAX: %f" % (minjetpt, maxjetpt)
    
    #iterate through each value in leaf of jet pts
    for i in range(leaf.GetLen()):
        curr_val = int (leaf.GetValue(i)) # get the value
        
        if (curr_val & (1 << BIT_TIGHT)):
            cntr_tight += 1
        if (curr_val & (1 << BIT_MEDIUM)):
            cntr_medium += 1
        if (curr_val & (1 << BIT_LOOSE)):
            cntr_loose += 1
    
   
   #if (minjetpt < 10.0):       
        #print "MIN: %f MAX: %f" % (minjetpt, maxjetpt)
    
    # get number of jets with jetpt > JETPT_THRESHOLD        
    numTight.Fill(cntr_tight) 
    numMedium.Fill(cntr_medium)
    numLoose.Fill(cntr_loose)     





'''

fill_Electron_chain(nentries, chain, leaf, numJets, minJet, maxJet)

Fills gives chain over nentries given. Iterates through leaf values to extract
numJets values to fill. Normalizes the numJets histogram.

'''

def fill_Electron_hist(chain, leaf, entry, numElectrons, minJet, maxJet, phileaf, etaleaf, lepton_vec):
    
    # counter for number of values per entry > JETPT_THRESHOLD
    cntr = 0
    
    # max & min vals, just make initial value
    maxjetpt = INVALID
    minjetpt = INVALID
    
    #tracker for phi
    maxpt_phi = INVALID
    maxpt_eta = INVALID
    
    #iterate through each value in leaf of jet pts
    for i in range(leaf.GetLen()):
        curr_val = leaf.GetValue(i) # get the value
        curr_phi = phileaf.GetValue(i)
        curr_eta = etaleaf.GetValue(i)

        
        # only care about values with > JETPT_THRESHOLD
        if ((curr_val > ELECTRON_THRESHOLD_LO) & (curr_val < ELECTRON_THRESHOLD_HI)):
            #print "JET PT VAL: %f" % curr_val # to see if in order
            cntr += 1
            lepton_vec.append((curr_val, curr_phi, curr_eta))
            
            if ((curr_val > maxjetpt) | (maxjetpt == INVALID)):
                maxjetpt = curr_val
                maxpt_phi = curr_phi
                maxpt_eta = curr_eta
                
            if ((curr_val < minjetpt) | (minjetpt == INVALID)):
                minjetpt = curr_val
             
    
    # get number of jets with jetpt > JETPT_THRESHOLD        
    numElectrons.Fill(cntr) 
    maxJet.Fill(maxjetpt)
    minJet.Fill(minjetpt)
    
    return (maxjetpt, maxpt_phi, maxpt_eta)
    


'''

fill_Muon_chain(nentries, chain, leaf, numJets, minJet, maxJet)

Fills gives chain over nentries given. Iterates through leaf values to extract
numJets values to fill. Normalizes the numJets histogram.

'''

def fill_Muon_hist(chain, leaf, entry, numMuons, minJet, maxJet, phileaf, etaleaf, lepton_vec):
    
    # counter for number of values per entry > JETPT_THRESHOLD
    cntr = 0
    
    # max & min vals, just make initial value
    maxjetpt = INVALID
    minjetpt = INVALID
    
    #tracker for phi
    maxpt_phi = INVALID
    maxpt_eta = INVALID
    
    #iterate through each value in leaf of jet pts
    for i in range(leaf.GetLen()):
        curr_val = leaf.GetValue(i) # get the value
        curr_phi = phileaf.GetValue(i)
        curr_eta = etaleaf.GetValue(i)
        
        # only care about values with > JETPT_THRESHOLD
        if ((curr_val > MUON_THRESHOLD_LO) & (curr_val < MUON_THRESHOLD_HI)):
            #print "JET PT VAL: %f" % curr_val # to see if in order
            cntr += 1
            lepton_vec.append((curr_val, curr_phi, curr_eta))
            
            if ((curr_val > maxjetpt) | (maxjetpt == INVALID)):
                maxjetpt = curr_val
                maxpt_phi = curr_phi
                maxpt_eta = curr_eta
            
            if ((curr_val < minjetpt) | (minjetpt == INVALID)):
                minjetpt = curr_val
                
   
    
    
    # get number of jets with jetpt > JETPT_THRESHOLD        
    numMuons.Fill(cntr) 
    maxJet.Fill(maxjetpt)
    minJet.Fill(minjetpt) 
    
    return (maxjetpt, maxpt_phi, maxpt_eta)



'''

fill_MET_chain(nentries, chain, leaf, numJets)

Fills gives chain over nentries given. Iterates through leaf values to extract
numJets values to fill. Normalizes the numJets histogram.

'''

def fill_MET_hist(chain, leaf, entry, MET, phileaf, etaleaf):
    
    # counter for number of values per entry > JETPT_THRESHOLD
    cntr = 0
    
    met_phi = INVALID
    met_eta = INVALID
    
    #iterate through each value in leaf of jet pts
    for i in range(leaf.GetLen()):
        curr_val = leaf.GetValue(i) # get the value     
        met_phi = phileaf.GetValue(i)
        met_eta = etaleaf.GetValue(i)
    
    # fill MET value     
    MET.Fill(curr_val) 
    
    return (curr_val, met_phi, met_eta)
    
    
    
    
    





