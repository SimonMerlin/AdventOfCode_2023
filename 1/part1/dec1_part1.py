import sys
import os
import time
f = open(os.path.join(sys.path[0], './../input.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

def main():
    res = 0
    for line in lines:
        numbers = [i for i in line if i.isdigit()]
        if len(numbers)==1:
            value = int(numbers[0]+numbers[0])
        else:
            value = int(numbers[0]+numbers[len(numbers)-1])
        res += value
    return res


start = time.perf_counter()
print(main())
end = time.perf_counter()
print(f"Executed in {((end - start)*1000):0.2f} milliseconds")
