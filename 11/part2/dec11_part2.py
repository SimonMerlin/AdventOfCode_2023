import os
import time

f = open(os.path.dirname(__file__) + '/../input.txt', 'r')
universe = [l.rstrip() for l in f.readlines()]

EXPANSION_RATIO = 1000000

def getEmptyRows(universe):
    return [r for r in range(len(universe)) if all([s=='.' for s in universe[r]])]

def getEmptyColumns(universe):
    return [c for c in range(len(universe[0])) if all([r[c]=='.' for r in universe])]

def countEmptyBetween(a, b, list):
    a, b = (a, b) if a<b else (b, a)
    return len([e for e in list if e>a and e<b])

def getGalaxies(universe):
    return [(x, y) for y in range(len(universe)) for x in range(len(universe[y])) if universe[y][x] == '#']

def getDistancesBetweenGalaxies(galaxies, emptyRows, emptyColumns):
    cpt=0
    for i in range(len(galaxies)):
        for j in range(len(galaxies)-i):
            countEmptyColumns = countEmptyBetween(galaxies[i][0], galaxies[j+i][0], emptyColumns)
            countEmptyRows = countEmptyBetween(galaxies[i][1], galaxies[j+i][1], emptyRows)
            deltaX = abs(galaxies[i][0] - galaxies[i+j][0]) - countEmptyColumns + countEmptyColumns*EXPANSION_RATIO
            deltaY = abs(galaxies[i][1] - galaxies[i+j][1]) - countEmptyRows + countEmptyRows*EXPANSION_RATIO
            cpt += deltaX + deltaY
    return cpt

def main():
    emptyRows, emptyColumns = getEmptyRows(universe), getEmptyColumns(universe)
    galaxies = getGalaxies(universe)
    return getDistancesBetweenGalaxies(galaxies, emptyRows, emptyColumns)

if __name__ == '__main__': 
    start = time.perf_counter()
    print(main())
    end = time.perf_counter()
    print(f"Executed in {((end - start)*1000):0.2f} milliseconds")