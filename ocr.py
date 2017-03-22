#!/usr/bin/env python

import sys
import argparse
from scipy.misc import imread, imfilter, imsave
from StringIO import StringIO

def process(infile, debug):
    im = imread(infile)
    ## Example process
    im_edge = imfilter(im, 'edge_enhance_more')
    if debug:
        imsave("debug-edge.png", im_edge)
    return 'Unknown'

def main():
    parser = argparse.ArgumentParser(description='7-segment OCR')
    parser.add_argument('-i', '--input', required=True, help='input file name, "-" for stdin')
    parser.add_argument('-d', '--debug', action='store_true', help='generate debug info and intermediate results')
    args = parser.parse_args()

    infile = open(args.input, 'rb') if args.input != '-' else StringIO(sys.stdin.read())
    print >> sys.stderr, process(infile, args.debug)

if __name__ == '__main__':
    main()
