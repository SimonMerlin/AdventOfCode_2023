import os
import time
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

f = open(os.path.dirname(__file__) + '/../input.txt', 'r')
lines = [l.rstrip() for l in f.readlines()]

def findStartCoordinates():
    for y in range(len(lines)):
        if 'S' in lines[y]:
            return lines[y].index('S'), y

def getNextPoint(current, previous):
    x, y = current[0], current[1]
    currentSymbol = lines[current[1]][current[0]]
    if currentSymbol =='F' :
        if previous[0] == x+1:
            return (x, y+1) if lines[y+1][x] in 'J|LS' else None
        return (x+1, y) if lines[y][x+1] in 'J-7S' else None
    if currentSymbol =='J':
        if previous[0] == x-1:
            return (x, y-1) if lines[y-1][x] in '7|FS' else None
        return (x-1, y) if lines[y][x-1] in 'L-FS' else None
    if currentSymbol =='7':
        if previous[0] == x-1:
            return (x, y+1) if lines[y+1][x] in 'J|LS' else None
        return (x-1, y) if lines[y][x-1] in 'L-FS' else None
    if currentSymbol =='L':
        if previous[0] == x+1:
            return (x, y-1) if lines[y-1][x] in '7|FS' else None
        return (x+1, y) if lines[y][x+1] in 'J-7S' else None
    if currentSymbol == '-':
        if previous[0] == x-1:
            return (x+1, y) if lines[y][x+1] in 'J-7S' else None
        return (x-1, y) if lines[y][x-1] in 'L-FS' else None
    if currentSymbol =='|':
        if previous[1] == y-1:
            return (x, y+1) if lines[y+1][x] in 'J|LS' else None
        return (x, y-1) if lines[y-1][x] in '7|FS' else None
    raise Exception("I don't know where to go ! I'm in {} from {}".format(current, previous))
    

def getAllStartingPoints(start):
    x, y = start[0], start[1]
    nextPoints = []
    if x>0 and lines[y][x-1] in 'L-FS': #go left
        nextPoints.append((x-1, y))
    if y>0 and lines[y-1][x] in '7|FS': #go up
        nextPoints.append((x, y-1))
    if x<len(lines[0])-1 and x<len(lines[0])-1 and lines[y][x+1] in 'J-7S': #go right
        nextPoints.append((x+1, y))
    if y<len(lines)-1 and lines[y+1][x] in 'J|LS': # go down
        nextPoints.append((x, y+1))
    return nextPoints

def getLoop(start, current, previous, path=[]):
    while current != start or len(path)==0:
        next = getNextPoint(current, previous)
        if next == None:
            return None
        path.append(next)
        previous = current
        current = next
    return path

def pointIsInside(p, loop, polygon):
    if p in loop:
        return False
    point = Point(p[0], p[1])
    return polygon.contains(point)

def main():
    start = findStartCoordinates()
    startingPoints = getAllStartingPoints(start)
    for s in startingPoints:
        loop = getLoop(start, s, start, [start, s])
        if loop != None :
            break
    pointsInside = 0
    polygon = Polygon(loop)
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if pointIsInside((x, y), loop, polygon):
                pointsInside += 1
    return pointsInside

if __name__ == '__main__': 
    start = time.perf_counter()
    print(main())
    end = time.perf_counter()
    print(f"Executed in {((end - start)*1000):0.2f} milliseconds")