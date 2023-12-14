import sys
import os
import time
f = open(os.path.join(sys.path[0], './../input.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

class Dish:
    def __init__(self, rows):
        self.rows = [[c for c in r] for r in rows]
    
    def __str__(self):
        return "\n".join(["".join(r) for r in self.rows])
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.rows == other.rows
        else:
            return False
        
    def __hash__(self):
        return hash(tuple(["".join(r) for r in self.rows]))
    
    def tilt(self, direction):
        if direction == 'N':
            for c in range(len(self.rows[0])):
                for r in range(len(self.rows)):
                    if self.rows[r][c] == 'O':
                        tmpR = r
                        while tmpR-1>=0 and self.rows[tmpR-1][c]=='.':
                            tmpR-=1
                        if tmpR != r:
                            self.rows[tmpR][c] = 'O'
                            self.rows[r][c] = '.'
        if direction == 'S':
            for c in range(len(self.rows[0])):
                for r in range(len(self.rows)-1, -1, -1):
                    if self.rows[r][c] == 'O':
                        tmpR = r
                        while tmpR+1<len(self.rows) and self.rows[tmpR+1][c]=='.':
                            tmpR+=1
                        if tmpR != r:
                            self.rows[tmpR][c] = 'O'
                            self.rows[r][c] = '.'
        if direction == 'W':
            for r in range(len(self.rows)):
                for c in range(len(self.rows[0])):
                    if self.rows[r][c] == 'O':
                        tmpC = c
                        while tmpC-1>=0 and self.rows[r][tmpC-1]=='.':
                            tmpC-=1
                        if tmpC != c:
                            self.rows[r][tmpC] = 'O'
                            self.rows[r][c] = '.'
        if direction == 'E':
            for r in range(len(self.rows)):
                for c in range(len(self.rows[0])-1, -1, -1):
                    if self.rows[r][c] == 'O':
                        tmpC = c
                        while tmpC+1<len(self.rows[0]) and self.rows[r][tmpC+1]=='.':
                            tmpC+=1
                        if tmpC != c:
                            self.rows[r][tmpC] = 'O'
                            self.rows[r][c] = '.'
    def doCycle(self):
        direction = 'NWSE'
        for d in direction:
                self.tilt(d)

    def getLoadValue(self):
        loadValue = 0
        for i in range(len(self.rows)):
            loadValue += "".join(self.rows[i]).count('O') * (len(self.rows)-i)
        return loadValue

def parseInput():
    return Dish(lines)

def main():
    dish = parseInput()
    nbCycles = 1000000000
    alreadySeenDish = dict()

    for i in range(1, nbCycles+1):
        dish.doCycle()
        if dish.__hash__() in alreadySeenDish:
            firstSeenDish = alreadySeenDish[dish.__hash__()]
            nbCyclesBetween = i - firstSeenDish
            nbCyclesToSkip = ((nbCycles - firstSeenDish)//nbCyclesBetween)*nbCyclesBetween
            nbLeftCycles = nbCycles - (nbCyclesToSkip + firstSeenDish)
            for _ in range(nbLeftCycles):
                dish.doCycle()
            return dish.getLoadValue()
        alreadySeenDish[dish.__hash__()] = i

start = time.perf_counter()
print(main())
end = time.perf_counter()
print(f"Executed in {((end - start)*1000):0.2f} milliseconds")