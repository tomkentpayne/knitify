#!/usr/bin/env python3
# knitify.py
"""
knitify.py
author: Thomas Payne
email: tomkentpayne@hotmail.com
licence: GPL v2
"""
from argparse import ArgumentParser
from pattern import Pattern

def parse_sys_args():
    parser = ArgumentParser(description='Generate knitting pattern from a bitmap image')
    parser.add_argument('bitmap' ,action='store')
    return parser.parse_args()

if __name__ == '__main__':
    bitmap_path = parse_sys_args().bitmap
    pattern = Pattern()
    print(bitmap_path)
