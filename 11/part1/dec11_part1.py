import os
import time

f = open(os.path.dirname(__file__) + '/../input.txt', 'r')
lines = [l.rstrip() for l in f.readlines()]

def expandUniverse():
    universe = []
    for r in lines:
        universe.append(r)
        if all([s=='.' for s in r]):
            universe.append(r)
    cAdded = 0
    for c in range(len(lines[0])):
        if all([r[c]=='.' for r in lines]):
            for i in range(len(universe)):
                universe[i] = universe[i][:c+cAdded] + '.' + universe[i][c+cAdded:]
            cAdded+=1
    return universe

def getGalaxies(universe):
    return [(x, y) for y in range(len(universe)) for x in range(len(universe[y])) if universe[y][x] == '#']

def getDistancesBetweenGalaxies(galaxies):
    return sum([abs(galaxies[i][0] - galaxies[j+i][0]) + abs(galaxies[i][1] - galaxies[j+i][1]) for i in range(len(galaxies)) for j in range(len(galaxies)-i)])

def main():
    global lines
    universe = expandUniverse()
    galaxies = getGalaxies(universe)
    return getDistancesBetweenGalaxies(galaxies)

if __name__ == '__main__': 
    start = time.perf_counter()
    print(main())
    end = time.perf_counter()
    print(f"Executed in {((end - start)*1000):0.2f} milliseconds")