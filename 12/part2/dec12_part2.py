import sys
import os
import time
import re
from itertools import product
import multiprocessing

f = open(os.path.join(sys.path[0], './../input.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

def getArrangementValue(row):
    return [len(v) for v in re.findall(r"#+", row)]

def countAllowedPattern(s, wantedValue):
    cpt = 0
    seq = list(s)

    # Find indices of char to replace
    indices = [i for i, c in enumerate(seq) if c=='?']
    #print("? = ", len(indices), 2**len(indices))
    # Generate key letter combinations & place them into the list
    for t in product('.#', repeat=len(indices)):
        for i, c in zip(indices, t):
            seq[i] = c
        newArr = ''.join(seq)
        value = getArrangementValue(newArr)
        if value == wantedValue:
            cpt+=1
    return cpt

def countAllowedPatternV2(s, wantedValue):
    cpt = 0
    seq = list(s)

    # Find indices of char to replace
    indices = [i for i, c in enumerate(seq) if c=='?']
    #print("? = ", len(indices), 2**len(indices))
    # Generate key letter combinations & place them into the list
    #stats = {'d#': 0, 'd.': 0, 'f#': 0, 'f.': 0}
    for t in product('.#', repeat=len(indices)):
        for i, c in zip(indices, t):
            seq[i] = c
        newArr = ''.join(seq)
        value = getArrangementValue(newArr)
        if value == wantedValue:
            cpt+=1
    #print(stats)

    return cpt
    

def countArrangements(s, wantedValue, unfoldRatio):
    value = countAllowedPatternV2(s, wantedValue)
    print("Initial : ", value)
    print()

    nextValue = countAllowedPatternV2(s+'.', wantedValue)
    print(". fin : ", nextValue)
    print()

    nextValue = countAllowedPatternV2(s+'#', wantedValue)
    print("# fin : ", nextValue)
    print()

    nextValue = countAllowedPatternV2('.'+s, wantedValue)
    print(". debut : ", nextValue)
    print()

    nextValue = countAllowedPatternV2('#'+s, wantedValue)
    print("# debut : ", nextValue)
    print()

    #get value for twice as big
    nextValue = countAllowedPatternV2(s+'?'+s, wantedValue+wantedValue)
    print("Unfold 2 : ", nextValue)
    print()

    #si se termine par . => after ; sinon before
    #growthRatio = 1
    #if s[-1]!='.':
        #growthRatio = countAllowedPattern(s+'?', wantedValue)
    #else:
        #growthRatio = countAllowedPattern('?'+s, wantedValue)
        #print("BEFORE : ", countAllowedPattern('?'+s, wantedValue))
        #print("AFTER : ", countAllowedPattern(s+'?', wantedValue))
    #print("growthRatio : ", growthRatio) 
    
    #print("HASHTAG : ", countAllowedPattern('#'+s, wantedValue))
    #print("POINT : ", countAllowedPattern('.'+s, wantedValue))
    #print("UNKNOW : ", countAllowedPattern('?'+s, wantedValue))
    

    #get growth ratio
    growthRatio = nextValue/value
    #print("Growth ratio : ", int(growthRatio))

    #get value for unfoldRatio
    for _ in range(unfoldRatio-1):
        value *= growthRatio
    #print(int(value))
    #print()
    return int(value)

def countArrangementsV2(s, wantedValue, unfoldRatio):
    # get stats
    stats = {'d#': 0, 'd.': 0, 'f#': 0, 'f.': 0}
    stats['f.'] = countAllowedPatternV2(s+'.', wantedValue)
    stats['f#'] = countAllowedPatternV2(s+'#', wantedValue)
    stats['d.'] = countAllowedPatternV2('.'+s, wantedValue)
    stats['d#'] = countAllowedPatternV2('#'+s, wantedValue)
    value = countAllowedPatternV2(s, wantedValue)
    lastWantedValue = wantedValue[-1]
    lastChars = s[-lastWantedValue:]

    print(stats)
    
    #if s[-1]=='#' and all(x in {'?', '#'} for x in lastChars) and (s[-1-len(lastChars)]=='.' or s[-1-len(lastChars)]=='?'):
        #nextValue = value*value
    #else:
        #nextValue = (stats['d#'] + stats['d.']) * (stats['f#'] + stats['f.'])
    
    # end by .
    if s[-1]=='.': 
        nextValue = value*(stats['d#'] + stats['d.'])
    # last chars are #
    elif s[-1]=='#' and all(x in {'?', '#'} for x in lastChars) and s[-1-len(lastChars)]=='.':
        nextValue = value*value
    else:
        nextValue = (stats['d#'] + stats['d.']) * (stats['f#'] + stats['f.'])

    #get growth ratio
    growthRatio = nextValue/value
    #print("Growth ratio : ", int(growthRatio))

    #get value for unfoldRatio
    for _ in range(unfoldRatio-1):
        value *= growthRatio
    print(int(value))
    print()
    return int(value)


def main(procnum, list, resultDict):
    s=0
    print("Proc#{}".format(procnum))
    for i, l in enumerate(list):
        print(i)
        key, val = l.split(' ')
        val = [int(v) for v in val.split(',')]
        s += sum([countArrangementsV2(key, val, 5)])
    print("Proc#{} : {}".format(procnum, s))
    resultDict[procnum] = s


def mainMultiprocess():
    nbProcess = 1
    jobs = []
    manager = multiprocessing.Manager()
    resultDict = manager.dict()
    for i in range(nbProcess):
        p = multiprocessing.Process(target=main, args=(i, lines[int(i*(len(lines)/nbProcess)):int((i+1)*(len(lines)/nbProcess))],  resultDict))
        jobs.append(p)
        p.start()

    for proc in jobs:
        proc.join()
    print(resultDict)
    return sum(resultDict.values())

if __name__ == '__main__':  
    start = time.perf_counter()
    print(mainMultiprocess())
    end = time.perf_counter()
    print(f"Executed in {((end - start)*1000):0.2f} milliseconds")