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
    
    PT_NBINS =  170
    PT_NLO = 0
    PT_NHI = 340
    
    JETPT_THRESHOLD_LO = 0 #GeV
    JETPT_THRESHOLD_HI = 10000
    
    INVALID = -1.0
    
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

    # TT
    
    # to loop over all entries in the tree:
    for e in range(tt_n_entries):
        entry = t_tt.GetEntry(e)
        
        # counter for number of values per entry > JETPT_THRESHOLD
        cntr = 0
        
        # max & min vals, just make initial value
        maxjetpt = INVALID
        minjetpt = INVALID
        
        #print "MIN: %f MAX: %f" % (minjetpt, maxjetpt)
        
        #iterate through each value in leaf of jet pts
        for i in range(leaf_tt.GetLen()):
            curr_val = leaf_tt.GetValue(i) # get the value
            
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
        numJets_tt.Fill(cntr) 
        
        max_jetpt_per_event_tt.Fill(maxjetpt)
        min_jetpt_per_event_tt.Fill(minjetpt)



    # QCD
    
    for e in range(qcd_n_entries):    
        entry = t_qcd.GetEntry(e)
        
        # counter for number of values per entry > JETPT_THRESHOLD
        cntr = 0
        
        # max & min vals, just make initial value
        maxjetpt = INVALID
        minjetpt = INVALID
        
        #iterate through each value in leaf of jet pts
        for i in range(leaf_qcd.GetLen()):
            curr_val = leaf_qcd.GetValue(i) # get the value
            
            # only care about values with > JETPT_THRESHOLD
            if ((curr_val > JETPT_THRESHOLD_LO) & (curr_val < JETPT_THRESHOLD_HI)):
                #print "JET PT VAL: %f" % curr_val # to see if in order
                cntr += 1
                
            if ((curr_val > maxjetpt) | (maxjetpt == INVALID)):
                maxjetpt = curr_val
            
            if ((curr_val < minjetpt) | (minjetpt == INVALID)):
                minjetpt = curr_val
         
            
        # get number of jets with jetpt > JETPT_THRESHOLD 
        numJets_qcd.Fill(cntr)
        
        max_jetpt_per_event_qcd.Fill(maxjetpt)
        min_jetpt_per_event_qcd.Fill(minjetpt)

    # WJET
    
    for e in range(wjet_n_entries):    
        t_wjet.GetEntry(e)
        
        # counter for number of values per entry > JETPT_THRESHOLD
        cntr = 0
        
        # max & min vals, just make initial value
        maxjetpt = INVALID #leaf_wjet.GetValue(0)
        minjetpt = INVALID #leaf_wjet.GetValue(0)
        
        
        
        #iterate through each value in leaf of jet pts
        for i in range(leaf_wjet.GetLen()):
            curr_val = leaf_wjet.GetValue(i) # get the value
            
            # only care about values with > JETPT_THRESHOLD
            if ((curr_val > JETPT_THRESHOLD_LO) & (curr_val < JETPT_THRESHOLD_HI)):
                #print "JET PT VAL: %f" % curr_val # to see if in order
                cntr += 1
                
            if ((curr_val > maxjetpt)  | (maxjetpt == INVALID)):
                maxjetpt = curr_val
            
            if ((curr_val < minjetpt) | (minjetpt == INVALID)):
                minjetpt = curr_val
                
                
            #if (curr_val < 10):
                #print maxjetpt
            
        
        
        # get number of jets with jetpt > JETPT_THRESHOLD 
        numJets_wjet.Fill(cntr)
        
        #if (maxjetpt > 0):
        max_jetpt_per_event_wjet.Fill(maxjetpt)
        
        #if (minjetpt > 0):
        min_jetpt_per_event_wjet.Fill(minjetpt)

    
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
    
    ctest = Canvas()
    numJets_wjet.Draw('HIST')
    ctest.SaveAs("wjetsnumjets.pdf")
    
    ################ MIN MAX STUFF
    
    # TT
    
    # normalize
    max_jetpt_per_event_tt.Scale(1/normtt)
    min_jetpt_per_event_tt.Scale(1/normtt)
    
    #print "GET INTEGRAL: %f" % numJets_wjet.integral()

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
    
    # normalize
    max_jetpt_per_event_qcd.Scale(1/normqcd)
    min_jetpt_per_event_qcd.Scale(1/normqcd)
    
    #print "GET INTEGRAL: %f" % numJets_wjet.integral()

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
    
    # normalize
    max_jetpt_per_event_wjet.Scale(1/normwjet)
    min_jetpt_per_event_wjet.Scale(1/normwjet)
    
    #print "GET INTEGRAL: %f" % numJets_wjet.integral()

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
    
    
    
    
    
    
    
    
