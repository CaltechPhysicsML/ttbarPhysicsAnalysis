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
import matplotlib.pyplot as plt

# self-written code imports

from parser_constants import * # get constants used in this file


def draw_JetPT(numJets_tt, maxjet_tt, minjet_tt, numJets_qcd, maxjet_qcd, minjet_qcd, numJets_wjet, maxjet_wjet, minjet_wjet):
  
    
    #set line colors
    numJets_tt.SetLineColor(4)
    numJets_qcd.SetLineColor(8)
    numJets_wjet.SetLineColor(2)
    
    numJets_tt.legendstyle = 'L'
    numJets_qcd.legendstyle = 'L'
    numJets_wjet.legendstyle = 'L'
    
       
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
    
    maxjet_tt.legendstyle = 'L'
    minjet_tt.legendstyle = 'L'
    
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
    
    maxjet_qcd.legendstyle = 'L'
    minjet_qcd.legendstyle = 'L' 
    
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
    
    maxjet_wjet.legendstyle = 'L'
    minjet_wjet.legendstyle = 'L'
    
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
    
    
    loose_tt.legendstyle = 'L'
    medium_tt.legendstyle = 'L'
    tight_tt.legendstyle = 'L'
    
    loose_qcd.legendstyle = 'L'
    medium_qcd.legendstyle = 'L'
    tight_qcd.legendstyle = 'L'
    
    loose_wjet.legendstyle = 'L'
    medium_wjet.legendstyle = 'L'
    tight_wjet.legendstyle = 'L'   
    
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
    

def draw_ElectronPT(numElectrons_tt, maxept_tt, minept_tt, numElectrons_qcd, maxept_qcd, minept_qcd, numElectrons_wjet, maxept_wjet, minept_wjet):

    #set line colors
    numElectrons_tt.SetLineColor(4)
    numElectrons_qcd.SetLineColor(8)
    numElectrons_wjet.SetLineColor(2)
    
    numElectrons_tt.legendstyle = 'L'
    numElectrons_qcd.legendstyle = 'L'
    numElectrons_wjet.legendstyle = 'L'
       
    
    #begin drawing stuff
    c1 = Canvas()
    numElectrons_wjet.SetStats(0)
    numElectrons_wjet.Draw('HIST')
    numElectrons_tt.Draw('HIST SAME')
    numElectrons_qcd.Draw('HIST SAME')
    
    
    #make legend
    l1 = Legend([numElectrons_tt, numElectrons_qcd, numElectrons_wjet], textfont = 42, textsize = .03)
    l1.Draw()
    
    #save as pdf
    c1.SaveAs("ElectronPT_numElectrons.pdf");
    
    
    
    ################ MIN MAX STUFF
    
    # TT
    
    #set line colors
    maxept_tt.SetLineColor(4)
    minept_tt.SetLineColor(8)  
    
    maxept_tt.legendstyle = 'L'
    minept_tt.legendstyle = 'L'
    
    #begin drawing stuff
    c2 = Canvas()
    minept_tt.SetStats(0)
    minept_tt.Draw('HIST')
    maxept_tt.Draw('HIST SAME')
    
    #make legend
    l2 = Legend([minept_tt, maxept_tt], textfont = 42, textsize = .03)
    l2.Draw()
    
    #save as pdf
    c2.SaveAs("ElectronPT_maxminpt_tt.pdf")
    
    # QCD
    
    #set line colors
    maxept_qcd.SetLineColor(4)
    minept_qcd.SetLineColor(8)  
    
    maxept_qcd.legendstyle = 'L'
    minept_qcd.legendstyle = 'L'
    
    #begin drawing stuff
    c3 = Canvas()
    
    maxept_qcd.SetStats(0)
    maxept_qcd.Draw('HIST')
    minept_qcd.Draw('HIST SAME')
    
    #make legend
    l3 = Legend([minept_qcd, maxept_qcd], textfont = 42, textsize = .03)
    l3.Draw()

    #save as pdf
    c3.SaveAs("ElectronPT_maxminpt_qcd.pdf")



    #WJET
    #set line colors
    maxept_wjet.SetLineColor(4)
    minept_wjet.SetLineColor(8) 
    
    maxept_wjet.legendstyle = 'L'
    minept_wjet.legendstyle = 'L' 
    
    #begin drawing stuff
    c4 = Canvas()
    
    minept_wjet.SetStats(0)
    minept_wjet.Draw('HIST')
    maxept_wjet.Draw('HIST SAME')
    
    #make legend
    l4 = Legend([minept_wjet, maxept_wjet], textfont = 42, textsize = .03)
    l4.Draw()
    
    #save as pdf
    c4.SaveAs("ElectronPT_maxminpt_wjet.pdf")
    
    
    #make the plots wait on screen
    #wait(True)


def draw_MuonPT(numMuons_tt, maxupt_tt, minupt_tt, numMuons_qcd, maxupt_qcd, minupt_qcd, numMuons_wjet, maxupt_wjet, minupt_wjet):

    #set line colors
    numMuons_tt.SetLineColor(4)
    numMuons_qcd.SetLineColor(8)
    numMuons_wjet.SetLineColor(2)
    
    numMuons_tt.legendstyle = 'L'
    numMuons_qcd.legendstyle = 'L'
    numMuons_wjet.legendstyle = 'L'
       
    
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
    c1.SaveAs("MuonPT_numMuons.pdf");
    
    
    
    ################ MIN MAX STUFF
    
    # TT
    
    #set line colors
    maxupt_tt.SetLineColor(4)
    minupt_tt.SetLineColor(8)  
    
    maxupt_tt.legendstyle = 'L'
    minupt_tt.legendstyle = 'L'
    
    #begin drawing stuff
    c2 = Canvas()
    minupt_tt.SetStats(0)
    minupt_tt.Draw('HIST')
    maxupt_tt.Draw('HIST SAME')
    
    #make legend
    l2 = Legend([minupt_tt, maxupt_tt], textfont = 42, textsize = .03)
    l2.Draw()
    
    #save as pdf
    c2.SaveAs("MuonPT_maxminpt_tt.pdf")
    
    # QCD
    
    #set line colors
    maxupt_qcd.SetLineColor(4)
    minupt_qcd.SetLineColor(8)  
    
    maxupt_qcd.legendstyle = 'L'
    minupt_qcd.legendstyle = 'L'
    
    #begin drawing stuff
    c3 = Canvas()
    
    maxupt_qcd.SetStats(0)
    maxupt_qcd.Draw('HIST')
    minupt_qcd.Draw('HIST SAME')
    
    #make legend
    l3 = Legend([minupt_qcd, maxupt_qcd], textfont = 42, textsize = .03)
    l3.Draw()

    #save as pdf
    c3.SaveAs("MuonPT_maxminpt_qcd.pdf")



    #WJET
    #set line colors
    maxupt_wjet.SetLineColor(4)
    minupt_wjet.SetLineColor(8)  
    
    maxupt_wjet.legendstyle = 'L'
    minupt_wjet.legendstyle = 'L'
    
    #begin drawing stuff
    c4 = Canvas()
    
    minupt_wjet.SetStats(0)
    minupt_wjet.Draw('HIST')
    maxupt_wjet.Draw('HIST SAME')
    
    #make legend
    l4 = Legend([minupt_wjet, maxupt_wjet], textfont = 42, textsize = .03)
    l4.Draw()
    
    #save as pdf
    c4.SaveAs("MuonPT_maxminpt_wjet.pdf")
    
    
    #make the plots wait on screen
    #wait(True)


def draw_MET(MET_tt, MET_qcd, MET_wjet):

    #set line colors
    MET_tt.SetLineColor(4)
    MET_qcd.SetLineColor(8)
    MET_wjet.SetLineColor(2)
    
    MET_tt.legendstyle = 'L'
    MET_qcd.legendstyle = 'L'
    MET_wjet.legendstyle = 'L'
       
    
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
    c1.SaveAs("MET.pdf");
    
    #make the plots wait on screen
    #wait(True)


def draw_MT(MT_tt, MT_qcd, MT_wjet):

    #set line colors
    MT_tt.SetLineColor(4)
    MT_qcd.SetLineColor(8)
    MT_wjet.SetLineColor(2)
       
    MT_tt.legendstyle = 'L'
    MT_qcd.legendstyle = 'L'
    MT_wjet.legendstyle = 'L'
    
    
    #begin drawing stuff
    c1 = Canvas()
    MT_qcd.SetStats(0)
    MT_qcd.Draw('HIST')
    MT_tt.Draw('HIST SAME')
    MT_wjet.Draw('HIST SAME')
    
    
    #make legend
    l1 = Legend([MT_tt, MT_qcd, MT_wjet], textfont = 42, textsize = .03)
    l1.Draw()
    
    #save as pdf
    c1.SaveAs("MT.pdf");
    
    #make the plots wait on screen
    #wait(True)
    
    

def draw_HT(HT_tt, HT_qcd, HT_wjet):

    #set line colors
    HT_tt.SetLineColor(4)
    HT_qcd.SetLineColor(8)
    HT_wjet.SetLineColor(2)
       
    HT_tt.legendstyle = 'L'
    HT_qcd.legendstyle = 'L'
    HT_wjet.legendstyle = 'L'
    
    
    #begin drawing stuff
    c1 = Canvas()
    HT_wjet.SetStats(0)
    HT_wjet.Draw('HIST')
    HT_tt.Draw('HIST SAME')
    HT_qcd.Draw('HIST SAME')
    
    
    #make legend
    l1 = Legend([HT_tt, HT_qcd, HT_wjet], textfont = 42, textsize = .03)
    l1.Draw()
    
    #save as pdf
    c1.SaveAs("HT.pdf");
    
    #make the plots wait on screen
    wait(True)
    
    
    
    
    
    
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    










