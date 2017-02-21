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

# PT vector is given by (px, py) where px = pt cos phi & py = pt sin phi
def get_pt_vector(pt_val, phi_val):
    return np.array([pt_val * math.cos( phi_val ), pt_val * math.sin( phi_val )])
 

def get_max_ptvector(pt1, phi1, pt2, phi2):
    if pt1 > pt2:
        return get_pt_vector(pt1, phi1)
    else:
        return get_pt_vector(pt2, phi2)
    

def get_mt(ept, ephi, upt, uphi, metpt, metphi):
    sumpt = ept + upt
    ptvec = get_max_ptvector(ept, ephi, upt, uphi)
    metvec = get_pt_vector(metpt, metphi)
    return (math.sqrt(2 * ((sumpt * metpt) - np.dot(ptvec, metvec))))


# get phi values between 0 and 2pi; output value between -pi and pi
def delta_phi(phi1, phi2):
    dphi = phi1 - phi2
    #x = -1 * np.sign(dphi) * (abs(dphi) % np.pi)  
    norm_ang = abs(dphi) % (2*np.pi)
    if (norm_ang == np.pi):
        return dphi
    elif (norm_ang < np.pi):
        return np.sign(dphi) * (abs(dphi) % np.pi)
    else:
        return -1 * np.sign(dphi) * (abs(dphi) % np.pi)
        



'''
print delta_phi(-1.5*np.pi, 0) / np.pi
print delta_phi(1.5*np.pi, 0) / np.pi
print delta_phi(0.5*np.pi, 0) / np.pi
print delta_phi(-0.5*np.pi, 0) / np.pi
print delta_phi(np.pi, 0) / np.pi
print delta_phi(-np.pi, 0) / np.pi
print delta_phi(-1, 0)
print delta_phi(1, 0)
'''    
    
    
    
    
    
    
    
        
