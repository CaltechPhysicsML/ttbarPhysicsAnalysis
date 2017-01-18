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

   
def main():

    # get files 
    f_tt = rt.TFile("../../../ttbar_data/ttbar_lepFilter_13TeV_313.root")
    f_qcd = rt.TFile("../../../ttbar_data/qcd_lepFilter_13TeV_10.root")
    f_wjet = rt.TFile("../../../ttbar_data/wjets_lepFilter_13TeV_3.root")
    
    # run functions you want here
    extract_JetPT(f_tt, f_qcd, f_wjet)
    extract_JetBTag(f_tt, f_qcd, f_wjet)
    extract_Electron(f_tt, f_qcd, f_wjet)
    extract_Muon(f_tt, f_qcd, f_wjet)
                 

if __name__ == "__main__":
    main();
    
    
    
    
    
    
    
    
