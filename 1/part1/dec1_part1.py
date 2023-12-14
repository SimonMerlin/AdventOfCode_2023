import os
import time
import re

f = open(os.path.dirname(__file__) + '/../input.txt', 'r')
lines = [l.rstrip() for l in f.readlines()]

def main():
    return sum([int(n[0]+n[len(n)-1]) for n in [re.findall(r"[1-9]", line) for line in lines]])

if __name__ == '__main__': 
    start = time.perf_counter()
    print(main())
    end = time.perf_counter()
    print(f"Executed in {((end - start)*1000):0.2f} milliseconds")
