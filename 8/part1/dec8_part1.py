import os
import time

f = open(os.path.dirname(__file__) + '/../input.txt', 'r')
lines = [l.rstrip() for l in f.readlines()]

def parseInput():
    return {key: tuple(v for v in val[1:-1].split(', ')) for key, val in [line.split(' = ') for line in lines[2:]]}


def countPath(paths, start, end, instructions):
    cpt = 0
    while start != end:
        start = paths[start][0 if instructions[cpt % len(instructions)] == 'L' else 1]
        cpt += 1
    return cpt

def main():
    return countPath(parseInput(), 'AAA', 'ZZZ', lines[0])

if __name__ == '__main__': 
    start = time.perf_counter()
    print(main())
    end = time.perf_counter()
    print(f"Executed in {((end - start)*1000):0.2f} milliseconds")