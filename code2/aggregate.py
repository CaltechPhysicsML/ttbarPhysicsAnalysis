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

# extract necessary functions from helper/analysis code
from JetPT_analysis import extract_JetPT
from JetBTag_analysis import extract_JetBTag
from ElectronPT_analysis import extract_Electron
from MuonPT_analysis import extract_Muon
from MET_analysis import extract_MET


'''

extract_JetPT(f_tt, f_qcd, f_wjet)

This is the general function dealing with Jet.PT data. Get trees from files and 
create histograms. Fill necessary trees, and create plots.

'''
   
def do_analysis(f_tt, f_qcd, f_wjet, analyze_this):
    
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
    fill_JetPT_tree(tt_n_entries, t_tt, leaf_tt, numJets_tt, min_jetpt_per_event_tt, max_jetpt_per_event_tt)
    fill_JetPT_tree(qcd_n_entries, t_qcd, leaf_qcd, numJets_qcd, min_jetpt_per_event_qcd, max_jetpt_per_event_qcd)
    fill_JetPT_tree(wjet_n_entries, t_wjet, leaf_wjet, numJets_wjet, min_jetpt_per_event_wjet, max_jetpt_per_event_wjet)
    
    




   
def main():

    # get files 
    f_tt = rt.TFile("../../../ttbar_data/ttbar_lepFilter_13TeV_313.root")
    f_qcd = rt.TFile("../../../ttbar_data/qcd_lepFilter_13TeV_10.root")
    f_wjet = rt.TFile("../../../ttbar_data/wjets_lepFilter_13TeV_3.root")
    
    # array of stuff needed to be analyzed
    want_leaves = ['Jet.PT', 'Jet.BTag', 'Electron.PT', 'MuonTight.PT', 'MissingET.MET']
    
    # bits to be set if want analyzed:
    # Jet.PT = 0 (rightmost binary bit)
    # Jet.BTag = 1
    # Electron.PT = 2
    # MuonTight.PT = 3
    # MissingET.MET = 4 (leftmost binary bit)
    
    leaf_bits = 0b11111
    
    # create dictionary associating set bits to possible leafs
    analyze_this = {n: want_leaves[n] for n in leaf_bits}
    
    
    # run functions you want here
    do_analysis(f_tt, f_qcd, f_wjet, analyze_this)
                 

if __name__ == "__main__":
    main();
    
    
    
    
    
    
    
    
