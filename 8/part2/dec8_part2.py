import os
import time
import math

f = open(os.path.dirname(__file__) + '/../input.txt', 'r')
lines = [l.rstrip() for l in f.readlines()]

def parseInput():
    return {key: tuple(v for v in val[1:-1].split(', ')) for key, val in [line.split(' = ') for line in lines[2:]]}

def getStartingNodes(paths):
    return [n for n in paths.keys() if n[-1]=='A']

def countLoopSizeFromStartToZ(paths, start, instructions):
    current, cpt = start, 0
    while current != start or cpt==0:
        current = paths[current][0 if instructions[cpt % len(instructions)] == 'L' else 1]
        if current[-1]=='Z':
            return cpt+1
        cpt+= 1

def main():
    paths = parseInput()
    starts = getStartingNodes(paths)
    return math.lcm(*[countLoopSizeFromStartToZ(paths, s, lines[0]) for s in starts])

if __name__ == '__main__': 
    start = time.perf_counter()
    print(main())
    end = time.perf_counter()
    print(f"Executed in {((end - start)*1000):0.2f} milliseconds")