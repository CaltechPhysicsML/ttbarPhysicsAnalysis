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
 

# get the max pf the two PTs and return the pt, phi tuple
def get_max_ptvector(pt1, phi1, pt2, phi2):
    if pt1 >= pt2:
        return get_pt_vector(pt1, phi1)
    else:
        return get_pt_vector(pt2, phi2)


# adds two PTs but handles case where if one of them is invalid
def sum_pt(pt1, pt2):
    if pt1 == INVALID:
        pt1 = 0
    if pt2 == INVALID:
        pt2 == 0
    return pt1 + pt2
   

#def get_mt(ept, ephi, upt, uphi, metpt, metphi):
#    sumpt = sum_pt(ept, upt)
#    ptvec = get_max_ptvector(ept, ephi, upt, uphi)
#    metvec = get_pt_vector(metpt, metphi)
#    return (math.sqrt(2 * abs((sumpt * metpt) - np.dot(ptvec, metvec))))


# mt is calculated using equation:
# MT = sqrt{ 2 * [(lepton pt x met pt) - dot product(lepton (pt, phi), met (pt, phi))]}
def get_mt(lpt, lphi, metpt, metphi):
    ptvec = get_pt_vector(lpt, lphi)
    metvec = get_pt_vector(metpt, metphi)
    return (math.sqrt(2 * ((lpt * metpt) - np.dot(ptvec, metvec))))


# get phi values between 0 and 2pi; output value between -pi and pi
def delta_phi(phi1, phi2):
    dphi = phi1 - phi2 
    norm_ang = abs(dphi) % (2*np.pi)
    if (norm_ang == np.pi):
        return np.pi
    elif (norm_ang < np.pi):
        return np.sign(dphi) * norm_ang
    else:
        return np.sign(dphi) * ((abs(dphi) % np.pi) - np.pi)
        
# calculate delta R from gives phi and eta values
# dR = sqrt (phi^2 + eta^2)
def delta_R(phi1, phi2, eta1, eta2):
    eta = eta1 - eta2
    phi = delta_phi(phi1, phi2)
    return np.sqrt(phi ** 2 + eta ** 2)
    

# get the minimum delta R between a given jet and the array of leptons
# lepvec consists of (pt, phi, eta) tuples
def min_deltaR_jetlep(jetphi, jeteta, lepvec):
    mindR = INVALID
    
    for lep in range(len(lepvec)):
        lepphi = lepvec[lep][1]
        lepeta = lepvec[lep][2]
        dR = delta_R(jetphi, lepphi, jeteta, lepeta)
        
        if ((dR < mindR) | (mindR < 0)):
            mindR = dR
    
    return mindR
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
       
    
    
    
    
        
