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

class leptons:


    # maybe just use a dictionary to initialize all this isntead? (eg analyze_this)
    # can update dictionary when iterating through each NENETRY (NOT leaf), and then update 
    # to dictionary. then for each nentry, reinitialize class and extract what you want
    
    #remember that MT requires HIGHEST pt one
    
    #again, this can only be used once per entry in nentries! Only initialize after
    # all required info has been filled into a dictionary or somethang
    
    def __init__(self, e_pt, e_phi, u_pt, u_phi, met_pt, met_phi):
        self.e_pt = e_pt
        self.e_phi = e_phi
        self.u_pt = u_pt
        self.u_phi = u_phi
        self.met_pt = met_pt
        self.met_phi = met_phi
        
    
    # electron pt value is unchanced if there is no electron
    def is_electron(self):
        if self.e_pt == INVALID:
            return 0
        else:
            return 1
        
        
    # muon pt value is unchanced if there is no electron
    def is_muon(self):
        if self.u_pt == INVALID:
            return 0
        else:
            return 1
            
    
    # PT vector is given by (px, py) where px = pt cos phi & py = pt sin phi
    def get_e_ptvector(self):
        return np.array([self.e_pt*math.cos(self.e_phi), self.e_pt*math.sin(self.e_phi)])
        
    
    # PT vector is given by (px, py) where px = pt cos phi & py = pt sin phi
    def get_u_ptvector(self):
        return np.array([self.u_pt*math.cos(self.u_phi), self.u_pt*math.sin(self.u_phi)])
        
    # PT vector is given by (px, py) where px = pt cos phi & py = pt sin phi
    def get_met_ptvector(self):
        return np.array([self.met_pt*math.cos(self.met_phi), self.met_pt*math.sin(self.met_phi)])
    
    def get_total_pt(self):
        return (self.e_pt + self.u_pt)    
    
    def get_total_ptvector(self):
        return (self.get_e_ptvector() + self.get_u_ptvector())
        
    
    def get_mt(self):
        return (math.sqrt(2 * ((self.get_total_pt() * self.met_pt) - np.dot(self.get_total_ptvector(), self.get_met_ptvector()))))
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
