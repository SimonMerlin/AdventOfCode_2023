import os
import time

f = open(os.path.dirname(__file__) + '/../input.txt', 'r')
lines = [l.rstrip() for l in f.readlines()]

class Lens:
    def __init__(self, label, focus):
        self.label = label
        self.focus = int(focus)

class Box:
    def __init__(self, i):
        self.i = i
        self.lensList = []
    
    def removeLens(self, label):
        self.lensList = list(filter(lambda l: l.label != label, self.lensList))
    
    def addOrReplace(self, label, focus):
        added = False
        newLens = Lens(label, focus)
        for i, l in enumerate(self.lensList):
            if l.label == label:
                self.lensList[i] = newLens
                added = True
        if not added:
            self.lensList.append(newLens)
    
    def getBoxValue(self):
        return sum([((self.i+1)*(j+1)*l.focus) for j, l in enumerate(self.lensList)])
    
def getHash(string, value=0):
    return value if len(string)==0 else getHash(string[1:], ((value + ord(string[0]))*17)%256)

def doStep(hashmap, step):
    if step[-1]=='-':
        boxIndex = getHash(step[:-1])
        if boxIndex in hashmap:
            hashmap[boxIndex].removeLens(step[:-1])
    else:
        label, focus = step.split('=')
        boxIndex = getHash(label)
        if boxIndex in hashmap:
            hashmap[boxIndex].addOrReplace(label, focus)
        else:
            box = Box(boxIndex)
            box.addOrReplace(label, focus)
            hashmap[boxIndex] = box

def main():
    hashmap = dict()
    for step in lines[0].split(','):
        doStep(hashmap, step)
    return sum([b.getBoxValue() for b in hashmap.values()])

if __name__ == '__main__': 
    start = time.perf_counter()
    print(main())
    end = time.perf_counter()
    print(f"Executed in {((end - start)*1000):0.2f} milliseconds")