import sys
import os
import time
f = open(os.path.join(sys.path[0], './../input.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

seeds = []
typeMap, valuesMap = dict(), dict()
seedsIntersect = []

class Mapping:
    def __init__(self, destRangeStart, srcRangeStart, rangeLength):
        self.destRangeStart = destRangeStart
        self.srcRangeStart = srcRangeStart
        self.rangeLength = rangeLength
    
    def getMapping(self, value):
        if value >= self.srcRangeStart and value < self.srcRangeStart+self.rangeLength:
            return self.destRangeStart + (value-self.srcRangeStart)
        return None

def getLocationRange():
    locationInterset = []
    mapping = valuesMap['location']
    for m in mapping:
        minl, maxl = m.srcRangeStart, m.srcRangeStart+m.rangeLength
        inserted = False
        for li in locationInterset:
            if minl>= li[0] and minl<= li[0]:
                newMax = max(li[1], maxl)
                li[1] = newMax
        if not inserted:
            locationInterset.append([minl, maxl])

    locationInterset.sort(key=lambda a: a[0])
    print(locationInterset)
    return locationInterset

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
    return seedsIntersect

def hasSeed(seed):
    for s in seedsIntersect:
        if s[0]<=seed and s[1]>seed:
            return True
    return False

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
        typeMap[destType] = srcType
        
        # source and destination mapping
        i+=1
        while i < len(lines) and lines[i] != '':
            destRangeStart, srcRangeStart, rangeLength = [int(r.strip()) for r in lines[i].split(' ')]
            fillMapValuesForType(destType, srcRangeStart, destRangeStart, rangeLength)
            i+=1
        i+=1

def findSeedForLocation(location):
    srcType, srcValue = 'location', location

    while srcType in typeMap.keys():
        destType = typeMap[srcType]
        destValue = None
        for m in valuesMap[srcType]:
            if destValue == None:
                destValue = m.getMapping(srcValue)
        if destValue == None:
            destValue = srcValue
        
        srcType, srcValue = destType, destValue
    return srcValue


def main():
    global seedsIntersect
    parseInput()

    seedsIntersect = getSeedsRange()

    max = 1000000000
    for a in range(0,max):
        seedValue = findSeedForLocation(a)
        if a%10000000 == 0:
            print(a, ' / ', max)
        if hasSeed(seedValue):
            return a
        
    

start = time.perf_counter()
print(main())
end = time.perf_counter()
print(f"Executed in {((end - start)*1000):0.2f} milliseconds")