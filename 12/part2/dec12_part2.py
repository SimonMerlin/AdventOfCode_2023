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
    

def countArrangements(s, wantedValue, unfoldRatio):
    value = countAllowedPattern(s, wantedValue)
    #print("Initial : ", value)

    #get value for twice as big
    nextValue = countAllowedPattern(s+'?'+s, wantedValue+wantedValue)
    #print("Unfold 2 : ", nextValue)

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


def main(procnum, list, resultDict):
    s=0
    print("Proc#{}".format(procnum))
    for i, l in enumerate(list):
        print("Proc#{} : {}".format(procnum, i))
        key, val = l.split(' ')
        val = [int(v) for v in val.split(',')]
        s += sum([countArrangements(key, val, 5)])
    print("Proc#{} : {}".format(procnum, s))
    resultDict[procnum] = s


#lines[i*(len(lines)/nbProcess):(i+1)*(len(lines)/nbProcess)], 
def mainMultiprocess():
    nbProcess = 10
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