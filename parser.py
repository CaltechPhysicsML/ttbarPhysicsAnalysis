import ROOT as rt
import numpy as np
import matplotlib.pyplot as plt
import seaborn

f_tt = rt.TFile("../ttbar_data/ttbar_lepFilter_13TeV_313.root")
f_qcd = rt.TFile("../ttbar_data/qcd_lepFilter_13TeV_10.root")
f_wjet = rt.TFile("../ttbar_data/wjets_lepFilter_13TeV_3.root")


#Masses for electrons and muons
mass_of_electron = np.float64(0.0005109989461) #eV/c
mass_of_muon = np.float64(0.1056583715) 

OBJECT_TYPES = ['Jets', 'Electron', 'MuonTight', 'Photon', 'MissingET', 'EFlowPhoton', 'EFlowNeutralHadron', 'EFlowTrack']
PT_ET_TYPES  = ['PT',          'PT',       'PT',      'MET',        'ET',           'ET',               'PT', ]
EXTRA_FILLS  = [['Charge'], ['Charge'],     [],        [],     ['Ehad', 'Eem'],  ['Ehad', 'Eem'], ['Charge','X', 'Y', 'Z', 'Dxy'],]
MASSES =    [mass_of_electron, mass_of_muon, 0,        0,           0,                0,                 0]
TRACK_MATCH =   [True,        True,        False,    False,        False,           False,              False]
COMPUTE_ISO =   [True,        True,        True,     False,        True,           True,              False]

ROOT_OBSERVS =  ['PT', 'ET', 'MET', 'Eta', 'Phi', 'Charge', 'X', 'Y', 'Z', 'Dxy', 'Ehad', 'Eem']
OUTPUT_OBSERVS =  ['Entry','E/c', 'Px', 'Py', 'Pz', 'PT_ET','Eta', 'Phi', 'Charge', 'X', 'Y', 'Z',\
                     'Dxy', 'Ehad', 'Eem', 'MuIso', 'EleIso', 'ChHadIso','NeuHadIso','GammaIso']
ISO_TYPES = [('MuIso', 'MuonTight'), ('EleIso','Electron'), ('ChHadIso','EFlowTrack') ,('NeuHadIso','EFlowNeutralHadron'),('GammaIso','EFlowPhoton')]


# Dannys
def delphes_parser(filepath):

    tree = f_tt.Get("Delphes")
    
    n_entries=tree.GetEntries()
        
        
     #Get all the leaves that we need to read and their associated branches
    leaves_by_object = {}
    for obj in OBJECT_TYPES:
        leaves_by_object[obj] = {}
        for observ in ROOT_OBSERVS:
            leaf = tree.GetLeaf(obj + '.' + observ)
            if(isinstance(leaf,rt.TLeafElement)):
                leaves_by_object[obj][observ] = (leaf, leaf.GetBranch())
                #print(leaf.GetBranch())
   
def simple_delphes_parser(filepath1, filepath2, filepath3):
    
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
    
    numJets_tt = []
    numJets_qcd = []
    numJets_wjet = []
    
    # ASSUMING THEY ALL HAVE THE SAME NUMBER OF ENTRIES
    # to loop over all entries in the tree:
    for e in range(tt_n_entries):
        t_tt.GetEntry(e)
        t_qcd.GetEntry(e)
        t_wjet.GetEntry(e)

        numJets_tt.append(leaf_tt.GetLen())
        numJets_qcd.append(leaf_qcd.GetLen())
        numJets_wjet.append(leaf_wjet.GetLen())
    
    plt.hist(numJets_tt, histtype = 'step', color = 'blue')
    plt.hist(numJets_qcd, histtype = 'step', color = 'red')
    plt.hist(numJets_wjet, histtype = 'step', color = 'green')
    plt.show()
    
    
   
def main():
    simple_delphes_parser(f_tt, f_qcd, f_wjet)
                 

if __name__ == "__main__":
    main();
    
    
    
    
    
    
    
    
