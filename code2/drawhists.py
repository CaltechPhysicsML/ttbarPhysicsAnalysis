# generic imports 

import ROOT as rt
import numpy as np
import math
import matplotlib.pyplot as plt
import seaborn
from rootpy.plotting import Hist, HistStack, Graph, Canvas, Legend
from rootpy.plotting.style import get_style, set_style
from rootpy.interactive import wait
from rootpy.plotting.utils import draw
import rootpy.plotting.root2matplotlib as rplt

# self-written code imports

from parser_constants import * # get constants used in this file


def draw_JetPT(numJets_tt, maxjet_tt, minjet_tt, numJets_qcd, maxjet_qcd, minjet_qcd, numJets_wjet, maxjet_wjet, minjet_wjet):

    #set line colors
    numJets_tt.SetLineColor(4)
    numJets_qcd.SetLineColor(8)
    numJets_wjet.SetLineColor(2)
       
    
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
    c1.SaveAs("jetpt_numjets.pdf");
    
    
    ################ MIN MAX STUFF
    
    # TT
    
    #set line colors
    maxjet_tt.SetLineColor(4)
    minjet_tt.SetLineColor(8)  
    
    #begin drawing stuff
    c2 = Canvas()
    minjet_tt.SetStats(0)
    minjet_tt.Draw('HIST')
    maxjet_tt.Draw('HIST SAME')
    
    #make legend
    l2 = Legend([minjet_tt, maxjet_tt], textfont = 42, textsize = .03)
    l2.Draw()
    
    #save as pdf
    c2.SaveAs("jetpt_maxminpt_tt.pdf")
    
    # QCD
    
    #set line colors
    maxjet_qcd.SetLineColor(4)
    minjet_qcd.SetLineColor(8)  
    
    #begin drawing stuff
    c3 = Canvas()
    
    minjet_qcd.SetStats(0)
    minjet_qcd.Draw('HIST')
    maxjet_qcd.Draw('HIST SAME')
    
    #make legend
    l3 = Legend([minjet_qcd, maxjet_qcd], textfont = 42, textsize = .03)
    l3.Draw()

    #save as pdf
    c3.SaveAs("jetpt_maxminpt_qcd.pdf")



    #WJET
    #set line colors
    maxjet_wjet.SetLineColor(4)
    minjet_wjet.SetLineColor(8)  
    
    #begin drawing stuff
    c4 = Canvas()
    
    minjet_wjet.SetStats(0)
    minjet_wjet.Draw('HIST')
    maxjet_wjet.Draw('HIST SAME')
    
    #make legend
    l4 = Legend([minjet_wjet, maxjet_wjet], textfont = 42, textsize = .03)
    l4.Draw()
    
    #save as pdf
    c4.SaveAs("jetpt_maxminpt_wjet.pdf")
    
    
    #make the plots wait on screen
    #wait(True)
    

def draw_JetBTag(loose_tt, medium_tt, tight_tt, loose_qcd, medium_qcd, tight_qcd, loose_wjet, medium_wjet, tight_wjet):

    #set line colors
    loose_tt.SetLineColor(4)
    medium_tt.SetLineColor(8)
    tight_tt.SetLineColor(2)
    
    loose_qcd.SetLineColor(4)
    medium_qcd.SetLineColor(8)
    tight_qcd.SetLineColor(2)
    
    loose_wjet.SetLineColor(4)
    medium_wjet.SetLineColor(8)
    tight_wjet.SetLineColor(2)
       
    
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
    c1.SaveAs("jetbtag_tt.pdf");
    
    
    
    c2 = Canvas()
    tight_qcd.SetStats(0)
    tight_qcd.Draw('HIST')
    medium_qcd.Draw('HIST SAME')
    loose_qcd.Draw('HIST SAME')
    
    
    #make legend
    l2 = Legend([tight_qcd, medium_qcd, loose_qcd], textfont = 42, textsize = .03)
    l2.Draw()
    
    #save as pdf
    c2.SaveAs("jetbtag_qcd.pdf");
    
    
    
    
    c3 = Canvas()
    tight_wjet.SetStats(0)
    tight_wjet.Draw('HIST')
    medium_wjet.Draw('HIST SAME')
    loose_wjet.Draw('HIST SAME')
    
    
    #make legend
    l3 = Legend([tight_wjet, medium_wjet, loose_wjet], textfont = 42, textsize = .03)
    l3.Draw()
    
    #save as pdf
    c3.SaveAs("jetbtag_wjet.pdf");
    
    #wait(True)
    





















