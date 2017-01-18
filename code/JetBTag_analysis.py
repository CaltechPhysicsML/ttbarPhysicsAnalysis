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

fill_JetBTag_tree(nentries, tree, leaf, numJets, minJet, maxJet)

Fills gives tree over nentries given. Iterates through leaf values to extract
numJets, minJet, and maxJet values to fill. Normalizes the numJets, minJet, 
and maxJet histograms.

'''

def fill_JetBTag_tree(nentries, tree, leaf, numLoose, numMedium, numTight):
    
    # to loop over all entries in the tree:
    for e in range(nentries):
        entry = tree.GetEntry(e)
        
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
        
    # get float version of num entries to normalize below; subtract 1 to get 
    # actual integral value of hist
    norm = float(nentries - 1)
    
    # normalize
    numTight.Scale(1/norm)
    numMedium.Scale(1/norm)
    numLoose.Scale(1/norm)




'''

extract_JetBTag(f_tt, f_qcd, f_wjet)

This is the general function dealing with Jet.PT data. Get trees from files and 
create histograms. Fill necessary trees, and create plots.

'''
   
def extract_JetBTag(f_tt, f_qcd, f_wjet):

    # get trees from files
    t_tt = f_tt.Get("Delphes")
    t_qcd = f_qcd.Get("Delphes")
    t_wjet = f_wjet.Get("Delphes")
    
    # get number of entries
    tt_n_entries = t_tt.GetEntries()
    qcd_n_entries = t_qcd.GetEntries()
    wjet_n_entries = t_wjet.GetEntries()
    
    # define leaves
    var_tt = "Jet.BTag"
    var_qcd = "Jet.BTag"
    var_wjet = "Jet.BTag"
    
    leaf_tt = t_tt.GetLeaf(var_tt)
    leaf_qcd = t_qcd.GetLeaf(var_qcd)
    leaf_wjet = t_wjet.GetLeaf(var_wjet)
   
    
    # create the histograms
    loose_tt = Hist(NBINS,NLO,NHI, title = 'loose_tt', legendstyle = 'L')
    medium_tt = Hist(NBINS,NLO,NHI, title = 'medium_tt', legendstyle = 'L')
    tight_tt = Hist(NBINS,NLO,NHI, title = 'tight_tt', legendstyle = 'L')
    
    loose_qcd = Hist(NBINS,NLO,NHI, title = 'loose_qcd', legendstyle = 'L')
    medium_qcd = Hist(NBINS,NLO,NHI, title = 'medium_qcd', legendstyle = 'L')
    tight_qcd = Hist(NBINS,NLO,NHI, title = 'tight_qcd', legendstyle = 'L')
    
    loose_wjet = Hist(NBINS,NLO,NHI, title = 'loose_wjet', legendstyle = 'L')
    medium_wjet = Hist(NBINS,NLO,NHI, title = 'medium_wjet', legendstyle = 'L')
    tight_wjet = Hist(NBINS,NLO,NHI, title = 'tight_wjet', legendstyle = 'L')

   
    # FILLING THE TREE
    fill_JetBTag_tree(tt_n_entries, t_tt, leaf_tt, loose_tt, medium_tt, tight_tt)
    fill_JetBTag_tree(qcd_n_entries, t_qcd, leaf_qcd, loose_qcd, medium_qcd, tight_qcd)
    fill_JetBTag_tree(wjet_n_entries, t_wjet, leaf_wjet, loose_wjet, medium_wjet, tight_wjet)
    
    #set line colors
    loose_tt.SetLineColor('blue')
    medium_tt.SetLineColor('green')
    tight_tt.SetLineColor('red')
    
    loose_qcd.SetLineColor('blue')
    medium_qcd.SetLineColor('green')
    tight_qcd.SetLineColor('red')
    
    loose_wjet.SetLineColor('blue')
    medium_wjet.SetLineColor('green')
    tight_wjet.SetLineColor('red')
       
    
    #begin drawing stuff
    c1 = Canvas()
    tight_tt.SetStats(0)
    tight_tt.Draw('HIST')
    medium_tt.Draw('HIST SAME')
    loose_tt.Draw('HIST SAME')
    
    
    #make legend
    l1 = Legend([tight_tt, medium_tt, loose_tt], textfont = 42, textsize = .03)
    l1.Draw()
    
    #save as pdf
    c1.SaveAs("../plots/JetBTag_plots/btag_tt.pdf");
    
    
    
    c2 = Canvas()
    tight_qcd.SetStats(0)
    tight_qcd.Draw('HIST')
    medium_qcd.Draw('HIST SAME')
    loose_qcd.Draw('HIST SAME')
    
    
    #make legend
    l2 = Legend([tight_qcd, medium_qcd, loose_qcd], textfont = 42, textsize = .03)
    l2.Draw()
    
    #save as pdf
    c2.SaveAs("../plots/JetBTag_plots/btag_qcd.pdf");
    
    
    
    
    c3 = Canvas()
    tight_wjet.SetStats(0)
    tight_wjet.Draw('HIST')
    medium_wjet.Draw('HIST SAME')
    loose_wjet.Draw('HIST SAME')
    
    
    #make legend
    l3 = Legend([tight_wjet, medium_wjet, loose_wjet], textfont = 42, textsize = .03)
    l3.Draw()
    
    #save as pdf
    c3.SaveAs("../plots/JetBTag_plots/btag_wjet.pdf");
    
    wait(True)
    
