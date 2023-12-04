import sys
import os
import time
f = open(os.path.join(sys.path[0], './../input.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

xMax, yMax = len(lines[0]), len(lines)

def getCoordinatesAround(x1, x2, y):
    coords = [(x1-1, y-1), (x1-1, y), (x1-1, y+1), (x2+1, y-1), (x2+1, y), (x2+1, y+1)]
    for x in range(x1, x2+1):
        coords.append((x, y-1))
        coords.append((x, y+1))
    return [c for c in coords if c[0]>=0 and c[0]<xMax and c[1]>=0 and c[1]<yMax]

def aroundIsEmpty(x1, x2, y):
    coords = getCoordinatesAround(x1, x2, y)
    return all([lines[c[1]][c[0]] == '.' for c in coords])

def main():
    counter = 0
    for y in range(yMax):
        for x in range(xMax):
            if lines[y][x] != '.' and (x-1<0 or (lines[y][x].isdigit() and not lines[y][x-1].isdigit()) or (not lines[y][x].isdigit() and lines[y][x-1].isdigit()) or lines[y][x-1] == '.'):
                value = lines[y][x]
                x1 = x
                while x+1<xMax and lines[y][x+1]!= '.' and lines[y][x+1].isdigit() and lines[y][x].isdigit():
                    x +=1
                    value += lines[y][x]
                if not aroundIsEmpty(x1, x, y) and value.isdigit():
                    counter += int(value)

    return counter

start = time.perf_counter()
print(main())
end = time.perf_counter()
print(f"Executed in {((end - start)*1000):0.2f} milliseconds")

