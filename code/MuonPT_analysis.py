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

fill_Muon_tree(nentries, tree, leaf, numJets, minJet, maxJet)

Fills gives tree over nentries given. Iterates through leaf values to extract
numJets values to fill. Normalizes the numJets histogram.

'''

def fill_Muon_tree(nentries, tree, leaf, numMuons, minJet, maxJet):
    
    # counter for no electrons
    noleaf = 0
    
    # to loop over all entries in the tree:
    for e in range(nentries):
        entry = tree.GetEntry(e)
        
        # counter for number of values per entry > JETPT_THRESHOLD
        cntr = 0
        
        # max & min vals, just make initial value
        maxjetpt = INVALID
        minjetpt = INVALID
        
        if leaf.GetLen() == 0:
            noleaf += 1
        
        #iterate through each value in leaf of jet pts
        for i in range(leaf.GetLen()):
            curr_val = leaf.GetValue(i) # get the value
            
            
            # only care about values with > JETPT_THRESHOLD
            if ((curr_val > ELECTRON_THRESHOLD_LO) & (curr_val < ELECTRON_THRESHOLD_HI)):
                #print "JET PT VAL: %f" % curr_val # to see if in order
                cntr += 1
                
            if ((curr_val > maxjetpt) | (maxjetpt == INVALID)):
                maxjetpt = curr_val
            
            if ((curr_val < minjetpt) | (minjetpt == INVALID)):
                minjetpt = curr_val
                
       
        
        
        # get number of jets with jetpt > JETPT_THRESHOLD        
        numMuons.Fill(cntr) 
        maxJet.Fill(maxjetpt)
        minJet.Fill(minjetpt) 
    
    print " "    
    print nentries 
    print noleaf
    print " "
    
        
    # get float version of num entries to normalize below; subtract 1 to get 
    # actual integral value of hist
    norm = float(nentries - 1)
    
    # normalize
    numMuons.Scale(1/norm)
    maxJet.Scale(1/norm)
    minJet.Scale(1/norm)


'''

extract_Muon(f_tt, f_qcd, f_wjet)

This is the general function dealing with Electron data. Get trees from files and 
create histograms. Fill necessary trees, and create plots.

'''
   
def extract_Muon(f_tt, f_qcd, f_wjet):
    
    # get trees from files
    t_tt = f_tt.Get("Delphes")
    t_qcd = f_qcd.Get("Delphes")
    t_wjet = f_wjet.Get("Delphes")
    
    # get number of entries
    tt_n_entries = t_tt.GetEntries()
    qcd_n_entries = t_qcd.GetEntries()
    wjet_n_entries = t_wjet.GetEntries()
    
    # define leaves
    var_tt = "MuonTight.PT"
    var_qcd = "MuonTight.PT"
    var_wjet = "MuonTight.PT"
    
    leaf_tt = t_tt.GetLeaf(var_tt)
    leaf_qcd = t_qcd.GetLeaf(var_qcd)
    leaf_wjet = t_wjet.GetLeaf(var_wjet)
   
    
    # create the histograms
    numMuons_tt = Hist(NBINS,NLO,NHI, title = 'numMuons_tt', legendstyle = 'L')
    numMuons_qcd = Hist(NBINS,NLO,NHI, title = 'numMuons_qcd', legendstyle = 'L')
    numMuons_wjet = Hist(NBINS,NLO,NHI, title = 'numMuons_wjet', legendstyle = 'L')
    
    # interesting values to plot
    max_upt_per_event_tt = Hist(PT_NBINS,PT_NLO,PT_NHI, title = 'Max MuonPT/Event tt', legendstyle = 'L')
    min_upt_per_event_tt = Hist(PT_NBINS,PT_NLO,PT_NHI, title = 'Min MuonPT/Event tt', legendstyle = 'L')
    
    max_upt_per_event_qcd = Hist(PT_NBINS,PT_NLO,PT_NHI, title = 'Max MuonPT/Event qcd', legendstyle = 'L')
    min_upt_per_event_qcd = Hist(PT_NBINS,PT_NLO,PT_NHI, title = 'Min MuonPT/Event qcd', legendstyle = 'L')
    
    max_upt_per_event_wjet = Hist(PT_NBINS,PT_NLO,PT_NHI, title = 'Max MuonPT/Event wjet', legendstyle = 'L')
    min_upt_per_event_wjet = Hist(PT_NBINS,PT_NLO,PT_NHI, title = 'Min MuonPT/Event wjet', legendstyle = 'L')

   
    # FILLING THE TREE
    fill_Muon_tree(tt_n_entries, t_tt, leaf_tt, numMuons_tt, min_upt_per_event_tt, max_upt_per_event_tt)
    fill_Muon_tree(qcd_n_entries, t_qcd, leaf_qcd, numMuons_qcd, min_upt_per_event_qcd, max_upt_per_event_qcd)
    fill_Muon_tree(wjet_n_entries, t_wjet, leaf_wjet, numMuons_wjet, min_upt_per_event_wjet, max_upt_per_event_wjet)
    
    #set line colors
    numMuons_tt.SetLineColor('blue')
    numMuons_qcd.SetLineColor('green')
    numMuons_wjet.SetLineColor('red')
       
    
    #begin drawing stuff
    c1 = Canvas()
    numMuons_wjet.SetStats(0)
    numMuons_wjet.Draw('HIST')
    numMuons_tt.Draw('HIST SAME')
    numMuons_qcd.Draw('HIST SAME')
    
    
    #make legend
    l1 = Legend([numMuons_tt, numMuons_qcd, numMuons_wjet], textfont = 42, textsize = .03)
    l1.Draw()
    
    #save as pdf
    c1.SaveAs("../plots/MuonPT_plots/numMuons.pdf");
    
    
    
    ################ MIN MAX STUFF
    
    # TT
    
    #set line colors
    max_upt_per_event_tt.SetLineColor('blue')
    min_upt_per_event_tt.SetLineColor('green')  
    
    #begin drawing stuff
    c2 = Canvas()
    min_upt_per_event_tt.SetStats(0)
    min_upt_per_event_tt.Draw('HIST')
    max_upt_per_event_tt.Draw('HIST SAME')
    
    #make legend
    l2 = Legend([min_upt_per_event_tt, max_upt_per_event_tt], textfont = 42, textsize = .03)
    l2.Draw()
    
    #save as pdf
    c2.SaveAs("../plots/MuonPT_plots/u_maxminpt_tt.pdf")
    
    # QCD
    
    #set line colors
    max_upt_per_event_qcd.SetLineColor('blue')
    min_upt_per_event_qcd.SetLineColor('green')  
    
    #begin drawing stuff
    c3 = Canvas()
    
    max_upt_per_event_qcd.SetStats(0)
    max_upt_per_event_qcd.Draw('HIST')
    min_upt_per_event_qcd.Draw('HIST SAME')
    
    #make legend
    l3 = Legend([min_upt_per_event_qcd, max_upt_per_event_qcd], textfont = 42, textsize = .03)
    l3.Draw()

    #save as pdf
    c3.SaveAs("../plots/MuonPT_plots/u_maxminpt_qcd.pdf")



    #WJET
    #set line colors
    max_upt_per_event_wjet.SetLineColor('blue')
    min_upt_per_event_wjet.SetLineColor('green')  
    
    #begin drawing stuff
    c4 = Canvas()
    
    min_upt_per_event_wjet.SetStats(0)
    min_upt_per_event_wjet.Draw('HIST')
    max_upt_per_event_wjet.Draw('HIST SAME')
    
    #make legend
    l4 = Legend([min_upt_per_event_wjet, max_upt_per_event_wjet], textfont = 42, textsize = .03)
    l4.Draw()
    
    #save as pdf
    c4.SaveAs("../plots/MuonPT_plots/u_maxminpt_wjet.pdf")
    
    
    #make the plots wait on screen
    wait(True)

