import sys
import os
import re
f = open(os.path.join(sys.path[0], './../data.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

regex = r"(?=(one|two|three|four|five|six|seven|eight|nine|[1-9]))"

numberAsString = {
    "one":"1",
    "two":"2",
    "three":"3",
    "four":"4",
    "five":"5",
    "six":"6",
    "seven":"7",
    "eight":"8",
    "nine":"9",
    }

def mapToNumber(number):
    if number.isdigit():
        return str(number)
    return numberAsString[number]

res = 0
for line in lines:
    matchs = re.findall(regex, line)
    if len(matchs)==1:
        value = int(mapToNumber(matchs[0])+mapToNumber(matchs[0]))
    else:
        value = int(mapToNumber(matchs[0])+mapToNumber(matchs[len(matchs)-1]))
    res += value
print(res)
    

    
