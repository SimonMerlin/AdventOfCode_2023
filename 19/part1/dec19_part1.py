import os
import time

f = open(os.path.dirname(__file__) + '/../input.txt', 'r')
lines = [l.rstrip() for l in f.readlines()]

workflows = dict()
parts = []

class Rule:
    def __init__(self, test=None, redirect=None):
        self.operation = None
        self.destination=None

        if test != None:
            self.key = test[0]
            operation, destination = test[1:].split(':')
            self.operation = operation
            self.destination=destination
        
        self.redirect=redirect
    
    def check(self, part):
        if self.redirect != None:
            return self.redirect
        
        value = part[self.key]
        if eval(str(value) + self.operation):
            return self.destination
        else:
            return None

class Workflow:
    def __init__(self, w):
        name, rulesStr = w.split('{')
        rulesStr = rulesStr[:-1]
        rules = []
        for r in rulesStr.split(','):
            if '<' in r or '>' in r:
                rule = Rule(test=r)
            else:
                rule = Rule(redirect=r)
            rules.append(rule)
        self.name=name
        self.rules=rules
    
    def check(self, part):
        for r in self.rules:
            res = r.check(part)
            if res != None:
                return res
            

def parsePart(part):
    partDict = dict()
    part = part[1:-1]
    for p in part.split(','):
        k, v = p.split('=')
        partDict[k] = int(v)
    return partDict

def isAccepted(part, wName):
    res = workflows[wName].check(part)
    if res=='A':
        return True
    if res=='R':
        return False
    else:
        return isAccepted(part, res)

def parseInput():
    global workflows, parts
    i=0
    while lines[i] != "":
        l= lines[i]
        name, _ = l.split('{')
        workflows[name] = Workflow(l)
        i+=1
    i+=1
    while i<len(lines):
        parts.append(parsePart(lines[i]))
        i+=1

def main():
    global workflows, parts
    parseInput()

    acceptedParts = []
    for p in parts:
        if isAccepted(p, 'in'):
            acceptedParts.append(p)
    
    return sum([v for p in acceptedParts for v in p.values()])

if __name__ == '__main__': 
    start = time.perf_counter()
    print(main())
    end = time.perf_counter()
    print(f"Executed in {((end - start)*1000):0.2f} milliseconds")