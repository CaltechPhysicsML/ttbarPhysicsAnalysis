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

fill_MET_tree(nentries, tree, leaf, numJets)

Fills gives tree over nentries given. Iterates through leaf values to extract
numJets values to fill. Normalizes the numJets histogram.

'''

def fill_MET_tree(nentries, tree, leaf, MET):
    
    
    # to loop over all entries in the tree:
    for e in range(nentries):
        entry = tree.GetEntry(e)
        
        # counter for number of values per entry > JETPT_THRESHOLD
        cntr = 0
        
        
        #iterate through each value in leaf of jet pts
        for i in range(leaf.GetLen()):
            curr_val = leaf.GetValue(i) # get the value     
        
        
        # fill MET value     
        MET.Fill(curr_val) 

        
    # get float version of num entries to normalize below; subtract 1 to get 
    # actual integral value of hist
    norm = float(nentries - 1)
    
    # normalize
    MET.Scale(1/norm)



'''

extract_Electron(f_tt, f_qcd, f_wjet)

This is the general function dealing with Electron data. Get trees from files and 
create histograms. Fill necessary trees, and create plots.

'''
   
def extract_MET(f_tt, f_qcd, f_wjet):
    
    # get trees from files
    t_tt = f_tt.Get("Delphes")
    t_qcd = f_qcd.Get("Delphes")
    t_wjet = f_wjet.Get("Delphes")
    
    # get number of entries
    tt_n_entries = t_tt.GetEntries()
    qcd_n_entries = t_qcd.GetEntries()
    wjet_n_entries = t_wjet.GetEntries()
    
    # define leaves
    var_tt = "MissingET.MET"
    var_qcd = "MissingET.MET"
    var_wjet = "MissingET.MET"
    
    leaf_tt = t_tt.GetLeaf(var_tt)
    leaf_qcd = t_qcd.GetLeaf(var_qcd)
    leaf_wjet = t_wjet.GetLeaf(var_wjet)
   
    
    # create the histograms
    MET_tt = Hist(MET_NBINS, MET_NLO, MET_NHI, title = 'MET_tt', legendstyle = 'L')
    MET_qcd = Hist(MET_NBINS, MET_NLO, MET_NHI, title = 'MET_qcd', legendstyle = 'L')
    MET_wjet = Hist(MET_NBINS, MET_NLO, MET_NHI, title = 'MET_wjet', legendstyle = 'L')

   
    # FILLING THE TREE
    fill_MET_tree(tt_n_entries, t_tt, leaf_tt, MET_tt)
    fill_MET_tree(qcd_n_entries, t_qcd, leaf_qcd, MET_qcd)
    fill_MET_tree(wjet_n_entries, t_wjet, leaf_wjet, MET_wjet)
    
    #set line colors
    MET_tt.SetLineColor('blue')
    MET_qcd.SetLineColor('green')
    MET_wjet.SetLineColor('red')
       
    
    #begin drawing stuff
    c1 = Canvas()
    MET_qcd.SetStats(0)
    MET_qcd.Draw('HIST')
    MET_tt.Draw('HIST SAME')
    MET_wjet.Draw('HIST SAME')
    
    
    #make legend
    l1 = Legend([MET_tt, MET_qcd, MET_wjet], textfont = 42, textsize = .03)
    l1.Draw()
    
    #save as pdf
    c1.SaveAs("../plots/MET_plots/MET.pdf");
    

    
    
    #make the plots wait on screen
    wait(True)

