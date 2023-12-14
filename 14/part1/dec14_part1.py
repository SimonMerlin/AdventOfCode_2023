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
    
    def tiltUp(self):
        for c in range(len(self.rows[0])):
            for r in range(len(self.rows)):
                if self.rows[r][c] == 'O':
                    tmpR = r
                    while tmpR-1>=0 and self.rows[tmpR-1][c]=='.':
                        tmpR-=1
                    if tmpR != r:
                        self.rows[tmpR][c] = 'O'
                        self.rows[r][c] = '.'
    
    def getLoadValue(self):
        loadValue = 0
        for i in range(len(self.rows)):
            loadValue += "".join(self.rows[i]).count('O') * (len(self.rows)-i)
        return loadValue

def parseInput():
    return Dish(lines)

def main():
    dish = parseInput()
    dish.tiltUp()
    return dish.getLoadValue()

start = time.perf_counter()
print(main())
end = time.perf_counter()
print(f"Executed in {((end - start)*1000):0.2f} milliseconds")