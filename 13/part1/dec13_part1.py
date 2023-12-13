import sys
import os
import time
f = open(os.path.join(sys.path[0], './../input.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

class Pattern:
    def __init__(self, rows):
        self.rows = rows
    
    def __str__(self):
        return "\n".join(self.rows)

    def findLineOfReflection(self):
        for i in range(len(self.rows)-1):
            if self.checkSymetry('H', i, i+1):
                return 'H', i, i+1
        for i in range(len(self.rows[0])-1):
            if self.checkSymetry('V', i, i+1):
                return 'V', i, i+1

    def checkSymetry(self, direction, a, b):
        if direction == 'H':
            while a>=0 and b<len(self.rows):
                if self.rows[a] != self.rows[b]:
                    return False
                a-=1
                b+=1
            return True
        else:
            while a>=0 and b<len(self.rows[0]):
                c1 = [self.rows[j][a] for j in range(len(self.rows))]
                c2 = [self.rows[j][b] for j in range(len(self.rows))]
                if c1 != c2:
                    return False
                a-=1
                b+=1
            return True


def parseInput():
    patterns = []
    rows = []
    i = 0
    while i<len(lines):
        if lines[i] == "":
            patterns.append(Pattern(rows))
            rows = []
        else:
            rows.append(lines[i])
        i+=1
    patterns.append(Pattern(rows))
    return patterns


def main():
    cpt = 0
    patterns = parseInput()
    for p in patterns:
        direction, a, b = p.findLineOfReflection()
        if direction == "V":
            cpt += a+1
        else:
            cpt += 100*(a+1)
    return cpt
start = time.perf_counter()
print(main())
end = time.perf_counter()
print(f"Executed in {((end - start)*1000):0.2f} milliseconds")