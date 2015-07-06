''' Pattern module for knitify '''
__author__ = 'Thomas Payne'
__email__ = 'tomkentpayne@hotmail.com'
__copyright__ = 'Copyright © 2015 Thomas Payne'
__licence__ = 'GPL v2'

import numpy as np
from scipy import misc

class Pattern(object):
    """A knitting pattern object generated from a bmp image"""
    def __init__(self):
        self.bitmap = None
        self.stitches = []
    def __str__(self):
        """Human-readable form of the pattern, i.e. to print and knit from"""
    def load_bitmap(self, bitmap_path):
        """Populate 2D stitches array from given bitmap"""
        self.bitmap = misc.imread(bitmap_path)
        if self.bitmap is None:
            raise FileNotFoundError('Image not found.')
        else:
            print("YAY")
        #example np array 5x5
        image_array = np.array(np.zeros([5,5]))
