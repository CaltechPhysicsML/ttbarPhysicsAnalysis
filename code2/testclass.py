class leptons:


    # maybe just use a dictionary to initialize all this isntead? (eg analyze_this)
    # can update dictionary when iterating through each NENETRY (NOT leaf), and then update 
    # to dictionary. then for each nentry, reinitialize class and extract what you want
    
    #remember that MT requires HIGHEST pt one
    
    #again, this can only be used once per entry in nentries! Only initialize after
    # all required info has been filled into a dictionary or somethang
    
    def __init__(self, e_pt, e_phi, u_pt, u_phi, met, met_phi):
        self.e_pt = e_pt
        self.e_phi = e_phi
        self.u_pt = u_pt
        self.u_phi = u_phi
        self.met = self.met
        self.met_phi = self.met_phi
        
    
    # electron pt value is unchanced if there is no electron
    def is_electron(self, e_pt):
        if e_pt = INVALID:
            return 0
        else
            return 1
        
        
    # muon pt value is unchanced if there is no electron
    def is_muon(self, u_pt):
        if u_pt = INVALID:
            return 0
        else
            return 1
            
    
    # PT vector is given by (px, py) where px = pt cos phi & py = pt sin phi
    def get_e_ptvector(self):
        return (self.e_pt*cos(self.e_phi), self.e_pt*sin(self.e_phi))
        
    
    # PT vector is given by (px, py) where px = pt cos phi & py = pt sin phi
    def get_u_ptvector(self):
        return (self.u_pt*cos(self.u_phi), self.u_pt*sin(self.u_phi))
        
    # PT vector is given by (px, py) where px = pt cos phi & py = pt sin phi
    def get_met_ptvector(self):
        return (self.met_pt*cos(self.met_phi), self.met_pt*sin(self.met_phi))
    
    def get_total_pt(self):
        return (e_pt + u_pt)    
    
    def get_total_ptvector(self)
        return (get_e_ptvector(self) + get_u_ptvector(self))
        
    
    def get_mt(self)
        return sqrt(2 * ((get_total_pt(self) * met_pt) - 
        np.dot(get_total_ptvector(self), get_met_ptvector(self))))
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
