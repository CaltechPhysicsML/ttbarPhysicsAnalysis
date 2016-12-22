import ROOT as rt
import numpy as np
import matplotlib.pyplot as plt
import seaborn
from rootpy.plotting import Hist, HistStack, Graph, Canvas, Legend
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
    
    
    numJets_tt = Hist(NBINS,NLO,NHI, title = 'numJets_tt', legendstyle = 'L')
    numJets_qcd = Hist(NBINS,NLO,NHI, title = 'numJets_qcd', legendstyle = 'L')
    numJets_wjet = Hist(NBINS,NLO,NHI, title = 'numJets_wjet', legendstyle = 'L')
    
    sumtt = 0
    sumqcd = 0
    sumwjet = 0
    
    # to loop over all entries in the tree:
    for e in range(tt_n_entries):
        entry = t_tt.GetEntry(e)
        numJets_tt.Fill(leaf_tt.GetLen())
        sumtt += leaf_tt.GetLen()
        #numJets_tt.append(leaf_tt.GetLen())
    
    for e in range(qcd_n_entries):    
        entry = t_qcd.GetEntry(e)
        numJets_qcd.Fill(leaf_qcd.GetLen())
        sumqcd += leaf_qcd.GetLen()
        #numJets_qcd.append(leaf_qcd.GetLen())
    
    for e in range(wjet_n_entries):    
        t_wjet.GetEntry(e)
        numJets_wjet.Fill(leaf_wjet.GetLen())
        sumwjet += leaf_wjet.GetLen()
        #numJets_wjet.append(leaf_wjet.GetLen())

    #print "HERE: sum: %d nentries: %d" % (sumtt, tt_n_entries)
   
    #normalize
    numJets_tt /= sumtt
    numJets_qcd /= sumqcd
    numJets_wjet /= sumwjet
    
    #set_style('ATLAS')
    
    
    #set line colors
    numJets_tt.SetLineColor('blue')
    numJets_qcd.SetLineColor('green')
    numJets_wjet.SetLineColor('red')
    
    
    #begin drawing stuff
    canvas = Canvas()
    stack = HistStack([numJets_tt, numJets_qcd, numJets_wjet], drawstyle='HIST')
    stack.Draw()
    
    #make legend
    l1 = Legend([numJets_tt, numJets_qcd, numJets_wjet], textfont = 42, textsize = .03)
    l1.Draw()
    canvas.Modified()
    canvas.Update()
    
    
    #numJets_tt.Draw()
    #numJets_qcd.Draw()
    #numJets_wjet.Draw() 
    
     
    #plt.show()
    wait(True)
    
    
   
def main():
    simple_delphes_parser(f_tt, f_qcd, f_wjet)
                 

if __name__ == "__main__":
    main();
    
    
    
    
    
    
    
    
