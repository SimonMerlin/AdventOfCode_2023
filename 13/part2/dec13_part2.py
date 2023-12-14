import os
import time

f = open(os.path.dirname(__file__) + '/../input.txt', 'r')
lines = [l.rstrip() for l in f.readlines()]

class Pattern:
    def __init__(self, rows):
        self.rows = rows
    
    def __str__(self):
        return "\n".join(self.rows)
    
    def findPotentialLineOfReflection(self):
        for i in range(len(self.rows)-1):
            if self.checkPotentialSymetry('H', i, i+1):
                return 'H', i, i+1
        for i in range(len(self.rows[0])-1):
            if self.checkPotentialSymetry('V', i, i+1):
                return 'V', i, i+1
        raise Exception(self.rows)
    
    def checkPotentialSymetry(self, direction, a, b):
        findSingleFix = False
        if direction == 'H':
            while a>=0 and b<len(self.rows):
                if countDiffBetweenList(self.rows[a] ,self.rows[b]) == 1 and not findSingleFix:
                    findSingleFix = True
                elif findSingleFix:
                    findSingleFix = findSingleFix and countDiffBetweenList(self.rows[a] ,self.rows[b])==0
                elif countDiffBetweenList(self.rows[a] ,self.rows[b]) != 0:
                    return False
                a-=1
                b+=1
        else:
            while a>=0 and b<len(self.rows[0]):
                c1 = [self.rows[j][a] for j in range(len(self.rows))]
                c2 = [self.rows[j][b] for j in range(len(self.rows))]
                if countDiffBetweenList(c1, c2) == 1 and not findSingleFix:
                    findSingleFix = True
                elif findSingleFix:
                    findSingleFix = findSingleFix and countDiffBetweenList(c1, c2)==0
                elif countDiffBetweenList(c1, c2)!= 0:
                    return False
                a-=1
                b+=1
        return findSingleFix


def countDiffBetweenList(l1, l2):
    return sum(i != j for i, j in zip(l1, l2))

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
    for i, p in enumerate(patterns):
        direction, a, _ = p.findPotentialLineOfReflection()
        if direction == "V":
            cpt += a+1
        else:
            cpt += 100*(a+1)
    return cpt

if __name__ == '__main__': 
    start = time.perf_counter()
    print(main())
    end = time.perf_counter()
    print(f"Executed in {((end - start)*1000):0.2f} milliseconds")