"""
pattern.py
author: Thomas Payne
email: tomkentpayne@hotmail.com
licence: GPL v2
"""
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
