import os
import time

f = open(os.path.dirname(__file__) + '/../input.txt', 'r')
lines = [l.rstrip() for l in f.readlines()]

def getPoints():
    nbPoints = 0
    coord = (0,0)
    x, y = [], []
    for l in lines:
        direction, length, _ = l.split(' ')
        length = int(length)
        if direction == 'R':
            coord = (coord[0]+length, coord[1])
        if direction == 'D':
            coord = (coord[0], coord[1]+length)
        if direction == 'L':
            coord = (coord[0]-length, coord[1])
        if direction == 'U':
            coord = (coord[0], coord[1]-length)
        nbPoints += length
        x.append(coord[0])
        y.append(coord[1])
    return x, y, nbPoints+1

def shoalaceV2(x, y):
    return abs(sum(x[i] * (y[i + 1] - y[i - 1]) for i in range(-1, len(x) - 1))) / 2.0

def main():
    x, y, exterior = getPoints()
    interior = shoelace(x, y)
    return int(interior + (exterior/2) + 1) #pick's formula

if __name__ == '__main__': 
    start = time.perf_counter()
    print(main())
    end = time.perf_counter()
    print(f"Executed in {((end - start)*1000):0.2f} milliseconds")