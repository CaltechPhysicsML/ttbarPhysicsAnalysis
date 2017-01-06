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

fill_tree(nentries, tree, leaf, numJets, minJet, maxJet)

Fills gives tree over nentries given. Iterates through leaf values to extract
numJets, minJet, and maxJet values to fill. Normalizes the numJets, minJet, 
and maxJet histograms.

'''

def fill_tree(nentries, tree, leaf, numJets, minJet, maxJet):
    
    # to loop over all entries in the tree:
    for e in range(nentries):
        entry = tree.GetEntry(e)
        
        # counter for number of values per entry > JETPT_THRESHOLD
        cntr = 0
        
        # max & min vals, just make initial value
        maxjetpt = INVALID
        minjetpt = INVALID
        
        #print "MIN: %f MAX: %f" % (minjetpt, maxjetpt)
        
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
        
        
       #if (minjetpt < 10.0):       
            #print "MIN: %f MAX: %f" % (minjetpt, maxjetpt)
        
        # get number of jets with jetpt > JETPT_THRESHOLD        
        numJets.Fill(cntr) 
        
        maxJet.Fill(maxjetpt)
        minJet.Fill(minjetpt) 
        
    # get float version of num entries to normalize below; subtract 1 to get 
    # actual integral value of hist
    norm = float(nentries - 1)
    
    # normalize
    numJets.Scale(1/norm)
    maxJet.Scale(1/norm)
    minJet.Scale(1/norm)

'''

simple_delphes_parser(f_tt, f_qcd, f_wjet)

This is the general function dealing with Jet.PT data. Get trees from files and 
create histograms. Fill necessary trees, and create plots.

'''
   
def simple_delphes_parser(f_tt, f_qcd, f_wjet):
    
    # get trees from files
    t_tt = f_tt.Get("Delphes")
    t_qcd = f_qcd.Get("Delphes")
    t_wjet = f_wjet.Get("Delphes")
    
    # get number of entries
    tt_n_entries = t_tt.GetEntries()
    qcd_n_entries = t_qcd.GetEntries()
    wjet_n_entries = t_wjet.GetEntries()
    
    # define leaves
    var_tt = "Jet.PT"
    var_qcd = "Jet.PT"
    var_wjet = "Jet.PT"
    
    leaf_tt = t_tt.GetLeaf(var_tt)
    leaf_qcd = t_qcd.GetLeaf(var_qcd)
    leaf_wjet = t_wjet.GetLeaf(var_wjet)
   
    
    # create the histograms
    numJets_tt = Hist(NBINS,NLO,NHI, title = 'numJets_tt', legendstyle = 'L')
    numJets_qcd = Hist(NBINS,NLO,NHI, title = 'numJets_qcd', legendstyle = 'L')
    numJets_wjet = Hist(NBINS,NLO,NHI, title = 'numJets_wjet', legendstyle = 'L')
    

    # interesting values to plot
    max_jetpt_per_event_tt = Hist(PT_NBINS,PT_NLO,PT_NHI, title = 'Max JetPT/Event tt', legendstyle = 'L')
    min_jetpt_per_event_tt = Hist(PT_NBINS,PT_NLO,PT_NHI, title = 'Min JetPT/Event tt', legendstyle = 'L')
    
    max_jetpt_per_event_qcd = Hist(PT_NBINS,PT_NLO,PT_NHI, title = 'Max JetPT/Event qcd', legendstyle = 'L')
    min_jetpt_per_event_qcd = Hist(PT_NBINS,PT_NLO,PT_NHI, title = 'Min JetPT/Event qcd', legendstyle = 'L')
    
    max_jetpt_per_event_wjet = Hist(PT_NBINS,PT_NLO,PT_NHI, title = 'Max JetPT/Event wjet', legendstyle = 'L')
    min_jetpt_per_event_wjet = Hist(PT_NBINS,PT_NLO,PT_NHI, title = 'Min JetPT/Event wjet', legendstyle = 'L')

   
    # FILLING THE TREE
    fill_tree(tt_n_entries, t_tt, leaf_tt, numJets_tt, min_jetpt_per_event_tt, max_jetpt_per_event_tt)
    fill_tree(qcd_n_entries, t_qcd, leaf_qcd, numJets_qcd, min_jetpt_per_event_qcd, max_jetpt_per_event_qcd)
    fill_tree(wjet_n_entries, t_wjet, leaf_wjet, numJets_wjet, min_jetpt_per_event_wjet, max_jetpt_per_event_wjet)
    
    #set line colors
    numJets_tt.SetLineColor('blue')
    numJets_qcd.SetLineColor('green')
    numJets_wjet.SetLineColor('red')
       
    
    #begin drawing stuff
    c1 = Canvas()
    numJets_wjet.SetStats(0)
    numJets_wjet.Draw('HIST')
    numJets_tt.Draw('HIST SAME')
    numJets_qcd.Draw('HIST SAME')
    
    
    #make legend
    l1 = Legend([numJets_tt, numJets_qcd, numJets_wjet], textfont = 42, textsize = .03)
    l1.Draw()
    
    #save as pdf
    c1.SaveAs("numjets.pdf");
    
    
    ################ MIN MAX STUFF
    
    # TT
    
    #set line colors
    max_jetpt_per_event_tt.SetLineColor('blue')
    min_jetpt_per_event_tt.SetLineColor('green')  
    
    #begin drawing stuff
    c2 = Canvas()
    min_jetpt_per_event_tt.SetStats(0)
    min_jetpt_per_event_tt.Draw('HIST')
    max_jetpt_per_event_tt.Draw('HIST SAME')
    
    #make legend
    l2 = Legend([min_jetpt_per_event_tt, max_jetpt_per_event_tt], textfont = 42, textsize = .03)
    l2.Draw()
    
    #save as pdf
    c2.SaveAs("maxminpt_tt.pdf")
    
    # QCD
    
    #set line colors
    max_jetpt_per_event_qcd.SetLineColor('blue')
    min_jetpt_per_event_qcd.SetLineColor('green')  
    
    #begin drawing stuff
    c3 = Canvas()
    
    min_jetpt_per_event_qcd.SetStats(0)
    min_jetpt_per_event_qcd.Draw('HIST')
    max_jetpt_per_event_qcd.Draw('HIST SAME')
    
    #make legend
    l3 = Legend([min_jetpt_per_event_qcd, max_jetpt_per_event_qcd], textfont = 42, textsize = .03)
    l3.Draw()

    #save as pdf
    c3.SaveAs("maxminpt_qcd.pdf")



    #WJET
    #set line colors
    max_jetpt_per_event_wjet.SetLineColor('blue')
    min_jetpt_per_event_wjet.SetLineColor('green')  
    
    #begin drawing stuff
    c4 = Canvas()
    
    min_jetpt_per_event_wjet.SetStats(0)
    min_jetpt_per_event_wjet.Draw('HIST')
    max_jetpt_per_event_wjet.Draw('HIST SAME')
    
    #make legend
    l4 = Legend([min_jetpt_per_event_wjet, max_jetpt_per_event_wjet], textfont = 42, textsize = .03)
    l4.Draw()
    
    #save as pdf
    c4.SaveAs("maxminpt_wjet.pdf")
    
    
    #make the plots wait on screen
    wait(True)
    
    
   
def main():

    # get files 
    f_tt = rt.TFile("../../ttbar_data/ttbar_lepFilter_13TeV_313.root")
    f_qcd = rt.TFile("../../ttbar_data/qcd_lepFilter_13TeV_10.root")
    f_wjet = rt.TFile("../../ttbar_data/wjets_lepFilter_13TeV_3.root")
    
    # run functions you want here
    simple_delphes_parser(f_tt, f_qcd, f_wjet)
                 

if __name__ == "__main__":
    main();
    
    
    
    
    
    
    
    
