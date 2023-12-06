import sys
import os
import time
import math

f = open(os.path.join(sys.path[0], './../input.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

def parseInput():
    time = int(lines[0].split(':')[1].replace(' ', ''))
    distance = int(lines[1].split(':')[1].replace(' ', ''))
    return time, distance

def countWayToWinForRace(time, dist):
    delta = (time*time) - 4*dist
    x1 = int((-time + math.sqrt(delta)) / -2)
    x2 = int((-time - math.sqrt(delta)) / -2)
    return x2 - x1

def main():
    time, distance = parseInput()
    return countWayToWinForRace(time, distance)

start = time.perf_counter()
print(main())
end = time.perf_counter()
print(f"Executed in {((end - start)*1000):0.2f} milliseconds")