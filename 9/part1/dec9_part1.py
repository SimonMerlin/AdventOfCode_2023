import sys
import os
import time
from functools import reduce
import operator

f = open(os.path.join(sys.path[0], './../input.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

def parseInput():
    global lines
    lines = [[int(v) for v in l.split(' ')] for l in lines]

def reduceList(l):
    return [l[i+1]-l[i] for i in range(len(l)-1)]

def extrapolateList(l):
    if all([v==0 for v in l]):
        return 0
    return l[-1] + extrapolateList(reduceList(l))

def main():
    parseInput()
    return sum([extrapolateList(l) for l in lines])

start = time.perf_counter()
print(main())
end = time.perf_counter()
print(f"Executed in {((end - start)*1000):0.2f} milliseconds")