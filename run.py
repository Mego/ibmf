#!/usr/bin/env python3

from ibmf import IBMF

try:
    import prog
except ImportError:
    prog = None
    print("Unable to open prog.py, exiting!")
    exit(1)

try:
    p = IBMF().add_filters(prog.filters)
except AttributeError:
    print("Unable to load filters from prog.py, exiting!")
    exit(2)

for c in p:
    print(bytes([c]).decode(), end='')