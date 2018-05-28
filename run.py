#!/usr/bin/env python3

from ibmf import IBMF
import argparse

parser = argparse.ArgumentParser(description='IBMF')
parser.add_argument("-u", "--unpossible", action='store_true', help='only one-line lambdas allowed as filters')
args = parser.parse_args()

if args.unpossible:
    try:
        with open('prog_unpossible.py') as prog:
            filters = [eval(line, {}, {}) for line in prog]
    except IOError:
        print("Unable to open prog_unpossible.py, exiting!")
else:
    try:
        import prog
        filters = prog.filters
    except ImportError:
        print("Unable to open prog.py, exiting!")
        exit(1)

try:
    p = IBMF().add_filters(filters)
except AttributeError:
    print("Unable to load filters from prog.py, exiting!")
    exit(2)

for c in p:
    print(bytes([c]).decode(), end='')
