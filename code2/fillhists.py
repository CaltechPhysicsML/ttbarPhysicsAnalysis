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

'''

fill_JetPT_hist(tree, leaf, numJets, minJet, maxJet)

Fills gives tree over nentries. Iterates through leaf values to extract
numJets, minJet, and maxJet values to fill. Normalizes the numJets, minJet, 
and maxJet histograms.

'''

def fill_JetPT_hist(tree, leaf, entry, numJets, minJet, maxJet, HTfill, HT):
    
    # counter for number of values per entry > JETPT_THRESHOLD
    cntr = 0
    
    # max & min vals, just make initial value
    maxjetpt = INVALID
    minjetpt = INVALID
    
    HT_total = 0
    
    #iterate through each value in leaf of jet pts
    for i in range(leaf.GetLen()):
        curr_val = leaf.GetValue(i) # get the value
        
        #print "i: %d CURR VAL: %f" % (i, curr_val)
        
        # only care about values with > JETPT_THRESHOLD
        if ((curr_val > JETPT_THRESHOLD_LO) & (curr_val < JETPT_THRESHOLD_HI)):
            #print "JET PT VAL: %f" % curr_val # to see if in order
            cntr += 1
            
        if ((curr_val > maxjetpt) | (maxjetpt == INVALID)):
            maxjetpt = curr_val
        
        if ((curr_val < minjetpt) | (minjetpt == INVALID)):
            minjetpt = curr_val
            
        if (HTfill):
            HT_total = HT_total + curr_val
    
    
   #if (minjetpt < 10.0):       
        #print "MIN: %f MAX: %f" % (minjetpt, maxjetpt)
    
    # get number of jets with jetpt > JETPT_THRESHOLD        
    numJets.Fill(cntr) 
    maxJet.Fill(maxjetpt)
    minJet.Fill(minjetpt) 
    
    if (HTfill):
        HT.Fill(HT_total)
        



'''

fill_JetBTag_hist(nentries, tree, leaf, numJets, minJet, maxJet)

Fills gives tree over nentries given. Iterates through leaf values to extract
numJets, minJet, and maxJet values to fill. Normalizes the numJets, minJet, 
and maxJet histograms.

'''

def fill_JetBTag_hist(tree, leaf, entry, numLoose, numMedium, numTight):

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

fill_Electron_tree(nentries, tree, leaf, numJets, minJet, maxJet)

Fills gives tree over nentries given. Iterates through leaf values to extract
numJets values to fill. Normalizes the numJets histogram.

'''

def fill_Electron_hist(tree, leaf, entry, numElectrons, minJet, maxJet, phileaf):
    
    # counter for number of values per entry > JETPT_THRESHOLD
    cntr = 0
    
    # max & min vals, just make initial value
    maxjetpt = INVALID
    minjetpt = INVALID
    
    #tracker for phi
    maxpt_phi = INVALID
    
    #iterate through each value in leaf of jet pts
    for i in range(leaf.GetLen()):
        curr_val = leaf.GetValue(i) # get the value
        
        
        # only care about values with > JETPT_THRESHOLD
        if ((curr_val > ELECTRON_THRESHOLD_LO) & (curr_val < ELECTRON_THRESHOLD_HI)):
            #print "JET PT VAL: %f" % curr_val # to see if in order
            cntr += 1
            
        if ((curr_val > maxjetpt) | (maxjetpt == INVALID)):
            maxjetpt = curr_val
            maxpt_phi = phileaf.GetValue(i)
            
        if ((curr_val < minjetpt) | (minjetpt == INVALID)):
            minjetpt = curr_val
             
    
    # get number of jets with jetpt > JETPT_THRESHOLD        
    numElectrons.Fill(cntr) 
    maxJet.Fill(maxjetpt)
    minJet.Fill(minjetpt)
    
    return (maxjetpt, maxpt_phi)
    


'''

fill_Muon_tree(nentries, tree, leaf, numJets, minJet, maxJet)

Fills gives tree over nentries given. Iterates through leaf values to extract
numJets values to fill. Normalizes the numJets histogram.

'''

def fill_Muon_hist(tree, leaf, entry, numMuons, minJet, maxJet, phileaf):
    
    # counter for number of values per entry > JETPT_THRESHOLD
    cntr = 0
    
    # max & min vals, just make initial value
    maxjetpt = INVALID
    minjetpt = INVALID
    
    #tracker for phi
    maxpt_phi = INVALID
    
    #iterate through each value in leaf of jet pts
    for i in range(leaf.GetLen()):
        curr_val = leaf.GetValue(i) # get the value
        
        
        # only care about values with > JETPT_THRESHOLD
        if ((curr_val > MUON_THRESHOLD_LO) & (curr_val < MUON_THRESHOLD_HI)):
            #print "JET PT VAL: %f" % curr_val # to see if in order
            cntr += 1
            
        if ((curr_val > maxjetpt) | (maxjetpt == INVALID)):
            maxjetpt = curr_val
            maxpt_phi = phileaf.GetValue(i)
        
        if ((curr_val < minjetpt) | (minjetpt == INVALID)):
            minjetpt = curr_val
            
   
    
    
    # get number of jets with jetpt > JETPT_THRESHOLD        
    numMuons.Fill(cntr) 
    maxJet.Fill(maxjetpt)
    minJet.Fill(minjetpt) 
    
    return (maxjetpt, maxpt_phi)



'''

fill_MET_tree(nentries, tree, leaf, numJets)

Fills gives tree over nentries given. Iterates through leaf values to extract
numJets values to fill. Normalizes the numJets histogram.

'''

def fill_MET_hist(tree, leaf, entry, MET, phileaf):
    
    # counter for number of values per entry > JETPT_THRESHOLD
    cntr = 0
    
    met_phi = INVALID
    
    #iterate through each value in leaf of jet pts
    for i in range(leaf.GetLen()):
        curr_val = leaf.GetValue(i) # get the value     
        met_phi = phileaf.GetValue(i)
    
    # fill MET value     
    MET.Fill(curr_val) 
    
    return (curr_val, met_phi)
    
    
    
    
    





