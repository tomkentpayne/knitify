''' Generate a pdf knittinf pattern + chart from a bitmap image '''
__author__ = 'Thomas Payne'
__email__ = 'tomkentpayne@hotmail.com'
__copyright__ = 'Copyright © 2015 Thomas Payne'
__licence__ = 'GPL v2'

from argparse import ArgumentParser
from pattern import Pattern

def parse_sys_args():
    ''' Parse arguments for bitmap path '''
    parser = ArgumentParser(description='Generate knitting pattern from a bitmap image')
    parser.add_argument('bitmap' ,action='store')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_sys_args()
    bitmap_path = args.bitmap
    pattern = Pattern()
    #Print arg for debug purposes
    print(bitmap_path)
