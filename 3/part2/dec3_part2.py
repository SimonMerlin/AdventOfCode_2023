import sys
import os
f = open(os.path.join(sys.path[0], './../data.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

xMax, yMax = len(lines[0]), len(lines)


def findFullNumber(x, y):
    c = [(x, y)]
    number = lines[y][x]
    x1 = x
    while x1-1>=0 and lines[y][x1-1].isdigit():
        number = lines[y][x1-1] + number
        c.append((x1-1, y))
        x1 -=1
    x2 = x
    while x2+1<xMax and lines[y][x2+1].isdigit():
        number = number + lines[y][x2+1]
        c.append((x2+1, y))
        x2 +=1
    return number, c

def getCoordinatesAround(x1, x2, y):
    coords = [(x1-1, y-1), (x1-1, y), (x1-1, y+1), (x2+1, y-1), (x2+1, y), (x2+1, y+1)]
    for x in range(x1, x2+1):
        coords.append((x, y-1))
        coords.append((x, y+1))
    return [c for c in coords if c[0]>=0 and c[0]<xMax and c[1]>=0 and c[1]<yMax]

def main():
    counter = 0
    for y in range(yMax):
        for x in range(xMax):
            if lines[y][x] == '*':
                coords = getCoordinatesAround(x, x, y)
                numbers = list()
                csUsed = []
                for c in coords:
                    if lines[c[1]][c[0]].isdigit() and not (c in csUsed):
                        n, cUsed = findFullNumber(c[0], c[1])
                        csUsed += cUsed
                        numbers.append(n)
                if len(numbers) == 2:
                    print(int(numbers[0]), int(numbers[1]))
                    counter += int(numbers[0]) * int(numbers[1])
    return counter

print(main())
