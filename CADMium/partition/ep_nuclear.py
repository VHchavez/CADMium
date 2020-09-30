"""
ep_nuclear.py
"""

def ep_nuclear(self):
    """
    Calculate nuclear potenteial energy components of Ep
    """

    self.Ep.Ep_pot =   self.grid.integrate( np.sum( self.na_frac, axis=1 ) * self.vb ) \
                     + self.grid.integrate( np.sum( self.nb_frac, axis=1 ) * self.va )