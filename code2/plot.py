# THIS FILE TAKES IN ALLHISTS.ROOT AND PLOTS THE HISTOGRAMS

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

# extract necessary functions from helper/analysis code
from drawhists import *




def output_plots(f):

    f.ls()
    
    # JET PT PLOTS
    
    ttnumjets = f.Get('ttnumJets') 
    ttmaxjet = f.Get('ttmax_jetpt_per_event')
    ttminjet = f.Get('ttmin_jetpt_per_event')
    
    qcdnumjets = f.Get('qcdnumJets')
    qcdmaxjet = f.Get('qcdmax_jetpt_per_event')
    qcdminjet = f.Get('qcdmin_jetpt_per_event')
    
    wjetnumjets = f.Get('wjetnumJets')
    wjetmaxjet = f.Get('wjetmax_jetpt_per_event')
    wjetminjet = f.Get('wjetmin_jetpt_per_event')
    
    draw_JetPT(ttnumjets, ttmaxjet, ttminjet, qcdnumjets, qcdmaxjet, qcdminjet, wjetnumjets, wjetmaxjet, wjetminjet)
    
    # JET BTAG PLOTS
    
    ttloose = f.Get('ttloose')
    ttmedium = f.Get('ttmedium')
    tttight = f.Get('tttight')
    
    qcdloose = f.Get('qcdloose')
    qcdmedium = f.Get('qcdmedium')
    qcdtight = f.Get('qcdtight')
    
    wjetloose = f.Get('wjetloose')
    wjetmedium = f.Get('wjetmedium')
    wjettight = f.Get('wjettight')
    
    draw_JetBTag(ttloose, ttmedium, tttight, qcdloose, qcdmedium, qcdtight, wjetloose, wjetmedium, wjettight)
    
    # ELECTRON PT PLOTS
    
    ttnumelectrons = f.Get('ttnumElectrons')
    ttmaxept = f.Get('ttmax_ept_per_event')
    ttminept = f.Get('ttmin_ept_per_event')
    
    qcdnumelectrons = f.Get('qcdnumElectrons')
    qcdmaxept = f.Get('qcdmax_ept_per_event')
    qcdminept = f.Get('qcdmin_ept_per_event')
    
    wjetnumelectrons = f.Get('wjetnumElectrons')
    wjetmaxept = f.Get('wjetmax_ept_per_event')
    wjetminept = f.Get('wjetmin_ept_per_event')
    
    draw_ElectronPT(ttnumelectrons, ttmaxept, ttminept, qcdnumelectrons, qcdmaxept, qcdminept, wjetnumelectrons, wjetmaxept, wjetminept)
    
    # MUON PT PLOTS
    
    ttnummuons = f.Get('ttnumMuons')
    ttmaxupt = f.Get('ttmax_upt_per_event')
    ttminupt = f.Get('ttmin_upt_per_event')
    
    qcdnummuons = f.Get('qcdnumMuons')
    qcdmaxupt = f.Get('qcdmax_upt_per_event')
    qcdminupt = f.Get('qcdmin_upt_per_event')
    
    wjetnummuons = f.Get('wjetnumMuons')
    wjetmaxupt = f.Get('wjetmax_upt_per_event')
    wjetminupt = f.Get('wjetmin_upt_per_event')
    
    draw_MuonPT(ttnummuons, ttmaxupt, ttminupt, qcdnummuons, qcdmaxupt, qcdminupt, wjetnummuons, wjetmaxupt, wjetminupt)
    
    
    # MET PLOTS
    
    ttMET = f.Get('ttMET')
    qcdMET = f.Get('qcdMET')
    wjetMET = f.Get('wjetMET')    
    
    draw_MET(ttMET, qcdMET, wjetMET)
    
    # MT PLOTS
    
    ttMT = f.Get('ttMT')
    qcdMT = f.Get('qcdMT')
    wjetMT = f.Get('wjetMT')    
    
    draw_MT(ttMT, qcdMT, wjetMT)
    
    # HT PLOTS
    
    ttHT = f.Get('ttHT')
    qcdHT = f.Get('qcdHT')
    wjetHT = f.Get('wjetHT')    
    
    draw_HT(ttHT, qcdHT, wjetHT)
    
    # DPHI (MET -> Lepton) PLOTS
    
    ttDPHI = f.Get('ttdphi')
    qcdDPHI = f.Get('qcddphi')
    wjetDPHI = f.Get('wjetdphi')    
    
    draw_DPHI(ttDPHI, qcdDPHI, wjetDPHI)
    
    
    
    
    

def main():

    f_default = rt.TFile('chainedhists.root')

    if (int(raw_input("\nUse default allhists.root file? (Press " +
    "'Enter' if ok or '0' to enter your own: ") or '1')):
        print "\nSetting default file..."
        f_in = f_default
    else:
        print "\nWARNING: Might not work if not in allhists.root format..."
        
        # Ask for file to add, or set to 0
        f_in = str(raw_input("\nEnter a file path here or press " +
        "'Enter' to skip/finish adding file: ")) or 0
        
        # Check if no files are added to f_in, and set to default
        if (f_in == 0 and len(f_in) == 0):
            print "\nSetting default file..."
            f_in = f_default
            
        # Invalid file type
        elif (f_in[len(f_in) - len('.root'):] != '.root'):
            print "\nERROR: Invalid file!!!"
            
        # All other cases, and add file to f_in if there is file to add
        else: 
            if(f_in):
                print "\nSetting given file..."
                f_in = rt.TFile(f_in)
            else:
                print "\nSetting default file..."
                f_in = f_default
        
    output_plots(f_in)
    

if __name__ == "__main__":
    main();


