import sys
import os
import time
import re
from itertools import product

f = open(os.path.join(sys.path[0], './../input.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

def getArrangementValue(row):
    return [len(v) for v in re.findall(r"#+", row)]

def countAllowedPattern(s, wantedValue):
    cpt = 0
    seq = list(s)

    # Find indices of char to replace
    indices = [i for i, c in enumerate(seq) if c=='?']
    # Generate key letter combinations & place them into the list
    for t in product('.#', repeat=len(indices)):
        for i, c in zip(indices, t):
            seq[i] = c
        newArr = ''.join(seq)
        value = getArrangementValue(newArr)
        if value == wantedValue:
            cpt+=1
    return cpt

def main():
    s=0
    for l in lines:
        key, val = l.split(' ')
        val = [int(v) for v in val.split(',')]
        s += sum([countAllowedPattern(key, val)])
    return s

start = time.perf_counter()
print(main())
end = time.perf_counter()
print(f"Executed in {((end - start)*1000):0.2f} milliseconds")