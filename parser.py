import ROOT as rt
import numpy as np
import matplotlib.pyplot as plt
import seaborn
from rootpy.plotting import Hist, HistStack, Graph, Canvas, Legend
from rootpy.plotting.style import get_style, set_style
from rootpy.interactive import wait
from rootpy.plotting.utils import draw
import rootpy.plotting.root2matplotlib as rplt



   
def simple_delphes_parser(f_tt, f_qcd, f_wjet):
    
    # DEFINE CONSTANTS HERE
    NBINS = 15
    NLO = 0
    NHI = 15
    
    JETPT_THRESHOLD = 30 #GeV
    
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
    

   
    # FILLING THE TREE

    # TT
    
    # to loop over all entries in the tree:
    for e in range(tt_n_entries):
        entry = t_tt.GetEntry(e)
        
        # counter for number of values per entry > JETPT_THRESHOLD
        cntr = 0
        
        #iterate through each value in leaf of jet pts
        for i in range(leaf_tt.GetLen()):
            curr_val = leaf_tt.GetValue(i) # get the value
            
            # only care about values with > JETPT_THRESHOLD
            if (curr_val > JETPT_THRESHOLD):
                #print "JET PT VAL: %f" % curr_val # to see if in order
                cntr += 1
        
        # get number of jets with jetpt > JETPT_THRESHOLD        
        numJets_tt.Fill(cntr) 
        #print "LENGTH: %f: " % lentt

    # QCD
    
    for e in range(qcd_n_entries):    
        entry = t_qcd.GetEntry(e)
        
        # counter for number of values per entry > JETPT_THRESHOLD
        cntr = 0
        
        #iterate through each value in leaf of jet pts
        for i in range(leaf_qcd.GetLen()):
            curr_val = leaf_qcd.GetValue(i) # get the value
            
            # only care about values with > JETPT_THRESHOLD
            if (curr_val > JETPT_THRESHOLD):
                #print "JET PT VAL: %f" % curr_val # to see if in order
                cntr += 1
        
        # get number of jets with jetpt > JETPT_THRESHOLD 
        numJets_qcd.Fill(cntr)

    # WJET
    
    for e in range(wjet_n_entries):    
        t_wjet.GetEntry(e)
        
        # counter for number of values per entry > JETPT_THRESHOLD
        cntr = 0
        
        #iterate through each value in leaf of jet pts
        for i in range(leaf_wjet.GetLen()):
            curr_val = leaf_wjet.GetValue(i) # get the value
            
            # only care about values with > JETPT_THRESHOLD
            if (curr_val > JETPT_THRESHOLD):
                #print "JET PT VAL: %f" % curr_val # to see if in order
                cntr += 1
        
        # get number of jets with jetpt > JETPT_THRESHOLD 
        numJets_wjet.Fill(cntr)

    
    # get float version of num entries to normalize below; subtract 1 to get 
    # actual integral value of hist
    normtt = float(tt_n_entries - 1)
    normqcd = float(qcd_n_entries - 1)
    normwjet = float(wjet_n_entries - 1)
    
    # normalize
    numJets_tt.Scale(1/normtt)
    numJets_qcd.Scale(1/normqcd)
    numJets_wjet.Scale(1/normwjet)
    
    #print "GET INTEGRAL: %f" % numJets_wjet.integral()

    #set line colors
    numJets_tt.SetLineColor('blue')
    numJets_qcd.SetLineColor('green')
    numJets_wjet.SetLineColor('red')
       
    
    #begin drawing stuff
    
    #canvas = Canvas()
    #stack = HistStack([numJets_wjet, numJets_tt, numJets_qcd], drawstyle='HIST')
    #stack.Draw()
    numJets_wjet.SetStats(0)
    numJets_wjet.Draw('HIST')
    numJets_tt.Draw('HIST SAME')
    numJets_qcd.Draw('HIST SAME')
    
    
    #make legend
    l1 = Legend([numJets_tt, numJets_qcd, numJets_wjet], textfont = 42, textsize = .03)
    l1.Draw()
    #canvas.Modified()
    #canvas.Update()
    
    
    #numJets_tt.Draw()
    #numJets_qcd.Draw()
    #numJets_wjet.Draw() 
    
     
    #plt.show()
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
    
    
    
    
    
    
    
    
