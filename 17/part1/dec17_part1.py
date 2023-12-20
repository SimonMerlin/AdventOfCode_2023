import os
import time

f = open(os.path.dirname(__file__) + '/../input.txt', 'r')
lines = [l.rstrip() for l in f.readlines()]

class Node:
    def __init__(self, value, x, y):
        self.x=x
        self.y=y
        self.value = value
    
    def setParent(self, parent):
        self.parent = parent
    
    def __eq__(self, other):
        return other.x==self.x and other.y==self.y


def AStar():
    startNode = Node(0,0,0)
    openList = [startNode]
    closedList = []
    while len(openList) != 0:
        node = openList.pop(0)
        closedList.append(node)

def getNeigbors(node):



def main():
    n1 = Node(0,0,0)
    n2 = Node(0,1,1)
    n3 = Node(89,0,0)
    nodes = [n1, n2]
    print(n3 in nodes)

if __name__ == '__main__': 
    start = time.perf_counter()
    print(main())
    end = time.perf_counter()
    print(f"Executed in {((end - start)*1000):0.2f} milliseconds")