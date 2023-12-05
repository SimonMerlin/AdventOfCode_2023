import sys
import os
import time
f = open(os.path.join(sys.path[0], './../input.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

seeds = []
typeMap, valuesMap = dict(), dict()

class Mapping:
    def __init__(self, destRangeStart, srcRangeStart, rangeLength):
        self.destRangeStart = destRangeStart
        self.srcRangeStart = srcRangeStart
        self.rangeLength = rangeLength
    
    def getMapping(self, value):
        if value >= self.srcRangeStart and value < self.srcRangeStart+self.rangeLength:
            return self.destRangeStart + (value-self.srcRangeStart)
        return None

def getSeedsRange():
    seedsIntersect = []
    i=0
    while i<len(seeds):
        minS, maxS = seeds[i], seeds[i]+seeds[i+1]
        inserted = False
        for si in seedsIntersect:
            if minS>= si[0] and minS<= si[0]:
                newMax = max(si[1], maxS)
                si[1] = newMax
        if not inserted:
            seedsIntersect.append([minS, maxS])
        i+=2
    print(seedsIntersect)
    return seedsIntersect


def fillMapValuesForType(type, destRangeStart, srcRangeStart, rangeLength):
    mappingList = []
    if type in valuesMap.keys():
        mappingList = valuesMap[type]
    mappingList.append(Mapping(destRangeStart, srcRangeStart, rangeLength))
    valuesMap[type] = mappingList


def parseInput():
    global seeds
    seeds = [int(s.strip()) for s in lines[0].split(':')[1].split(' ') if s != '']

    i=2
    while i < len(lines):
        # type mapping
        srcType, destType = lines[i].split(' ')[0].split('-to-')
        typeMap[srcType] = destType
        
        # source and destination mapping
        i+=1
        while i < len(lines) and lines[i] != '':
            destRangeStart, srcRangeStart, rangeLength = [int(r.strip()) for r in lines[i].split(' ')]
            fillMapValuesForType(srcType, destRangeStart, srcRangeStart, rangeLength)
            i+=1
        i+=1

def findMinLOcationForSeedRange(seedMin, seedMax):
    minLocation = None
    for s in range(seedMin, seedMax):
        print(s-seedMin, '/', seedMax-seedMin)
        srcType, srcValue = 'seed', s

        while srcType in typeMap.keys():
            destType = typeMap[srcType]
            destValue = None
            for m in valuesMap[srcType]:
                if destValue == None:
                    destValue = m.getMapping(srcValue)
            if destValue == None:
                destValue = srcValue
            
            srcType, srcValue = destType, destValue

        if minLocation == None or minLocation>srcValue:
            minLocation = srcValue
    return minLocation


def main():
    minLocation = None
    parseInput()
    print("INPUT PARSED")

    seedsIntersect = getSeedsRange()
    print("SEEDS RANGE COMPUTED")
    print(len(seedsIntersect))

    for si in seedsIntersect:
        minForRange = findMinLOcationForSeedRange(si[0], si[1])
        if minLocation == None or minLocation>minForRange:
            minLocation = minForRange
        
    return minLocation
    

start = time.perf_counter()
print(main())
end = time.perf_counter()
print(f"Executed in {((end - start)*1000):0.2f} milliseconds")