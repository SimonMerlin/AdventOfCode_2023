import os
import time
import copy

f = open(os.path.dirname(__file__) + '/../input.txt', 'r')
lines = [l.rstrip() for l in f.readlines()]

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
    
    def __str__(self):
        return f"RULE; op: {self.operation}; dest: {self.destination}; red: {self.redirect}"
    def __repr__(self):
        return f"RULE ; op: {self.operation} ; dest: {self.destination} ; red: {self.redirect}"

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

def parseInput():
    i=0
    workflows = dict()
    while lines[i] != "":
        l= lines[i]
        name, _ = l.split('{')
        workflows[name] = Workflow(l)
        i+=1
    return workflows

def getRulesLeadToA(workflows, start):
    chainsToDo = []
    chainsEnd = []
    for r in workflows[start].rules:
        chainsToDo.append([[start, r]])
    while len(chainsToDo) != 0:
        chain = chainsToDo.pop(0) # get chain
        last = chain[-1] # get last [workflow, rule]
        if last[1].redirect == 'A' or last[1].destination == 'A': # if rule is valis path
            chainsEnd.append(chain)
        elif last[1].redirect == 'R' or last[1].destination == 'R': # if not valie path
            pass
        else: # else try next value in the path
            if last[1].redirect != None:
                dest = last[1].redirect
            else:
                dest = last[1].destination
            chainsToDo += [chain+[[dest, r]] for r in workflows[dest].rules]
    return chainsEnd

def printAChain(chain):
    s = chain[0][0]
    for c in chain :
        if c[1].redirect == 'A' or c[1].destination == 'A':
            s += ' -> ' + 'A'
        elif c[1].redirect == 'R' or c[1].destination == 'R':
            s += ' -> ' + 'R'
        else:
            if c[1].redirect != None:
                dest = c[1].redirect
            else:
                dest = c[1].destination
            s += ' -> ' + dest
    return s

def main():
    workflows = parseInput()
    paths = getRulesLeadToA(workflows, 'in')
    for c in paths:
        print(printAChain(c))
    

if __name__ == '__main__': 
    start = time.perf_counter()
    print(main())
    end = time.perf_counter()
    print(f"Executed in {((end - start)*1000):0.2f} milliseconds")