import importlib
import time
import timeit

def import_from(module, name):
    return getattr(importlib.import_module(module), name)

def computePerformance(function, nbTry):
    avg = 0
    for i in range(1, nbTry+1):
        start = time.perf_counter()
        res = function()
        end = time.perf_counter()
        avg += (end - start)
        print(f"{i}/{nbTry} ; Result : {res}")
    print(f"Execution average time {((end - start)*1000):0.2f} milliseconds")


def testFunctionPerformance():
    day = int(input("Day : "))
    if day<1 or day>25:
        raise Exception("Day should be between 1 and 25")
    part = int(input("Part : "))
    if part<1 or part>2:
        raise Exception("Part should be 1 or 2")
    nbTry = int(input("Number of try : "))
    
    folder = '{}.part{}.'.format(day, part)
    fileName = 'dec{}_part{}'.format(day, part)

    main = import_from(folder+fileName, 'main')
    computePerformance(main, nbTry)

if __name__ == '__main__':  
    testFunctionPerformance()