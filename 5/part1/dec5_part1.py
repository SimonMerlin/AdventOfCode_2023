import sys
import os
import time
f = open(os.path.join(sys.path[0], './../input.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

class Mapping:
    def __init__(self, destRangeStart, srcRangeStart, rangeLength):
        self.destRangeStart = destRangeStart
        self.srcRangeStart = srcRangeStart
        self.rangeLength = rangeLength
    
    def getMapping(self, value):
        if value >= self.srcRangeStart and value < self.srcRangeStart+self.rangeLength:
            return self.destRangeStart + (value-self.srcRangeStart)
        return None


seeds = []
typeMap, valuesMap = dict(), dict()

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


def main():
    minLocation = None
    parseInput()
    i = 0
    for s in seeds:
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
    

start = time.perf_counter()
print(main())
end = time.perf_counter()
print(f"Executed in {((end - start)*1000):0.2f} milliseconds")