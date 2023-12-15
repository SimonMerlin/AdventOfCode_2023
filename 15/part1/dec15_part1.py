import os
import time

f = open(os.path.dirname(__file__) + '/../input.txt', 'r')
lines = [l.rstrip() for l in f.readlines()]

def getHash(string, value=0):
    return value if len(string)==0 else getHash(string[1:], ((value + ord(string[0]))*17)%256)

def main():
    return sum([getHash(s) for s in lines[0].split(',')])

if __name__ == '__main__': 
    start = time.perf_counter()
    print(main())
    end = time.perf_counter()
    print(f"Executed in {((end - start)*1000):0.2f} milliseconds")