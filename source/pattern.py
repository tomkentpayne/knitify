''' Pattern module for knitify '''
__author__ = 'Thomas Payne'
__email__ = 'tomkentpayne@hotmail.com'
__copyright__ = 'Copyright © 2015 Thomas Payne'
__licence__ = 'GPL v2'
class Pattern(object):
    """A knitting pattern object generated from a bmp image"""
    def __init__(self):
        self.bitmap = None
        self.stitches = []
    def __str__(self):
        """Human-readable form of the pattern, i.e. to print and knit from"""
    def load_bitmap(self, bitmap_path):
        """Populate 2D stitches array from given bitmap"""
        pass
