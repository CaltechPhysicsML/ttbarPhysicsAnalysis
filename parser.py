import ROOT as rt
import numpy as np
import matplotlib.pyplot as plt
import seaborn
from rootpy.plotting import Hist, HistStack, Graph, Canvas
from rootpy.plotting.style import get_style, set_style
from rootpy.interactive import wait
from rootpy.plotting.utils import draw
import rootpy.plotting.root2matplotlib as rplt


f_tt = rt.TFile("../../ttbar_data/ttbar_lepFilter_13TeV_313.root")
f_qcd = rt.TFile("../../ttbar_data/qcd_lepFilter_13TeV_10.root")
f_wjet = rt.TFile("../../ttbar_data/wjets_lepFilter_13TeV_3.root")

   
def simple_delphes_parser(filepath1, filepath2, filepath3):
    
    # DEFINE CONSTANTS HERE
    NBINS = 15
    NLO = 1
    NHI = 15
    
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
    
    #numJets_tt = []
    #numJets_qcd = []
    #numJets_wjet = []
    
    
    numJets_tt = Hist(NBINS,NLO,NHI)
    numJets_qcd = Hist(NBINS,NLO,NHI)
    numJets_wjet = Hist(NBINS,NLO,NHI)
    
    
    
    # to loop over all entries in the tree:
    for e in range(tt_n_entries):
        entry = t_tt.GetEntry(e)
        numJets_tt.Fill(leaf_tt.GetLen())
        #numJets_tt.append(leaf_tt.GetLen())
    
    for e in range(qcd_n_entries):    
        entry = t_qcd.GetEntry(e)
        numJets_qcd.Fill(leaf_qcd.GetLen())
        #numJets_qcd.append(leaf_qcd.GetLen())
    
    for e in range(wjet_n_entries):    
        t_wjet.GetEntry(e)
        numJets_wjet.Fill(leaf_wjet.GetLen())
        #numJets_wjet.append(leaf_wjet.GetLen())

   
    #normalize
    numJets_tt /= tt_n_entries
    numJets_qcd /= qcd_n_entries
    numJets_wjet /= wjet_n_entries
    
    #set_style('ATLAS')
    
    
    #set line colors
    numJets_tt.SetLineColor('blue')
    numJets_qcd.SetLineColor('green')
    numJets_wjet.SetLineColor('red')
    
    
    #begin drawing stuff
    canvas = Canvas()
    stack = HistStack([numJets_tt, numJets_qcd, numJets_wjet], drawstyle='HIST')
    stack.Draw()
    
    
    #numJets_tt.Draw()
    #numJets_qcd.Draw()
    #numJets_wjet.Draw() 
    
     
    #plt.show()
    wait(True)
    
    
   
def main():
    simple_delphes_parser(f_tt, f_qcd, f_wjet)
                 

if __name__ == "__main__":
    main();
    
    
    
    
    
    
    
    
