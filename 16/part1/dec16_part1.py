import os
import time

f = open(os.path.dirname(__file__) + '/../input.txt', 'r')
lines = [l.rstrip() for l in f.readlines()]

maxX, maxY = None, None

class Grid:
    def __init__(self, grid):
        self.grid = grid
        self.energizedCells = []
    
    def getCell(self, x, y):
        return self.grid[y][x]
    
    def isEnergized(self, x, y, d):
        return (x, y, d) in self.energizedCells
    
    def setEnergizedCell(self, x, y, d):
        self.energizedCells.append((x, y, d))
    
    def countEnergizedCells(self):
        return len(set([(e[0], e[1]) for e in self.energizedCells]))
    
    def toString(self, energized):
        v = ""
        energizedC = set([(e[0], e[1]) for e in self.energizedCells])
        for y in range(len(self.grid)):
            r = self.grid[y]
            for x in range(len(r)):
                if not energized:
                    v += self.grid[y][x]
                else:
                    if (x, y) in energizedC:
                        v += '#'
                    else:
                        v += '.'
            v += '\n'
        return v

def getNextCoord(x, y, d, grid, likeEmpty=False):
    if grid.getCell(x, y) == '.' or likeEmpty:
        if d=='u':
            return x, y-1, d
        if d=='d':
            return x, y+1, d
        if d=='l':
            return x-1, y, d
        if d=='r':
            return x+1, y, d
    if grid.getCell(x, y) == '/':
        if d=='u':
            return x+1, y, 'r'
        if d=='d':
            return x-1, y, 'l'
        if d=='l':
            return x, y+1, 'd'
        if d=='r':
            return x, y-1, 'u'
    if grid.getCell(x, y) == '\\':
        if d=='u':
            return x-1, y, 'l'
        if d=='d':
            return  x+1, y, 'r'
        if d=='l':
            return x, y-1, 'u'
        if d=='r':
            return x, y+1, 'd'

def checkBeam(x, y, d, grid):
    toCheck = [(x, y, d)]
    while len(toCheck) != 0:
        x, y, d = toCheck.pop(0)
        if y<maxY and y>=0 and x>=0 and x<maxX and not grid.isEnergized(x, y, d):
            grid.setEnergizedCell(x, y, d)
            if grid.getCell(x, y) in './\\':
                nextX, nextY, nextD = getNextCoord(x, y, d, grid)
                toCheck.append((nextX, nextY, nextD))
            else:
                if (grid.getCell(x, y)=='|' and d in ('ud')) or (grid.getCell(x, y)=='-' and d in ('lr')):
                    nextX, nextY, nextD = getNextCoord(x, y, d, grid, True)
                    toCheck.append((nextX, nextY, nextD))
                elif grid.getCell(x, y)=='|' and d in ('lr'):
                    toCheck.append((x, y-1, 'u'))
                    toCheck.append((x, y+1, 'd'))
                elif grid.getCell(x, y)=='-' and d in ('ud'):
                    toCheck.append((x-1, y, 'l'))
                    toCheck.append((x+1, y, 'r'))

def main():
    global maxX, maxY
    maxX, maxY = len(lines[0]), len(lines)
    grid = Grid(lines)
    checkBeam(0, 0,'r', grid)
    return grid.countEnergizedCells()

if __name__ == '__main__': 
    start = time.perf_counter()
    print(main())
    end = time.perf_counter()
    print(f"Executed in {((end - start)*1000):0.2f} milliseconds")