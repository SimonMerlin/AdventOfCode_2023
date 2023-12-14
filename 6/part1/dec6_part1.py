import os
import time
from functools import reduce
import operator

f = open(os.path.dirname(__file__) + '/../input.txt', 'r')
lines = [l.rstrip() for l in f.readlines()]

def parseInput():
    times = [int(t.strip()) for t in lines[0].split(':')[1].split(' ') if t != '']
    distances = [int(t.strip()) for t in lines[1].split(':')[1].split(' ') if t != '']
    return list(zip(times, distances))

def countWayToWinForRace(time, dist):
    return sum([dist<(time-hold)*hold for hold in range(time)])


def main():
    races = parseInput()
    return reduce(operator.mul, [countWayToWinForRace(r[0], r[1]) for r in races], 1)

if __name__ == '__main__': 
    start = time.perf_counter()
    print(main())
    end = time.perf_counter()
    print(f"Executed in {((end - start)*1000):0.2f} milliseconds")