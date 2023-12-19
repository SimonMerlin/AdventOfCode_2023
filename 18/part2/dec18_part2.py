import os
import time

f = open(os.path.dirname(__file__) + '/../input.txt', 'r')
lines = [l.rstrip() for l in f.readlines()]

def getPoints():
    coord = (0,0)
    x, y = [0], [0]
    nbPoints = 1
    
    for l in lines:
        _, _, color = l.split(' ')
        length, direction = color[2:7], color[-2]
        length = int(length, 16)
        if direction == '0':
            coord = (coord[0]+length, coord[1])
        if direction == '1':
            coord = (coord[0], coord[1]+length)
        if direction == '2':
            coord = (coord[0]-length, coord[1])
        if direction == '3':
            coord = (coord[0], coord[1]-length)
        nbPoints += length
        x.append(coord[0])
        y.append(coord[1])
    return x, y, nbPoints

def shoalaceV2(x, y):
    return abs(sum(x[i] * (y[i + 1] - y[i - 1]) for i in range(-1, len(x) - 1))) / 2.0

def main():
    x, y, exterior = getPoints()
    interior = shoalaceV2(x, y)
    return int(interior + (exterior/2) + 1) #pick's formula

if __name__ == '__main__': 
    start = time.perf_counter()
    print(main())
    end = time.perf_counter()
    print(f"Executed in {((end - start)*1000):0.2f} milliseconds")