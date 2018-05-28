#!/usr/bin/env python3

from ibmf import IBMF

filters = [
    lambda i, x: b"Hello, World!\n"[i]
]

for c in IBMF().add_filters(filters):
    print(bytes([c]).decode(), end='')
