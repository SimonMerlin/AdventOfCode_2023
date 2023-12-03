import sys
import os
f = open(os.path.join(sys.path[0], './../data.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

res = 0
for line in lines:
    numbers = [i for i in line if i.isdigit()]
    if len(numbers)==1:
        value = int(numbers[0]+numbers[0])
    else:
        value = int(numbers[0]+numbers[len(numbers)-1])
    res += value
print(res)
