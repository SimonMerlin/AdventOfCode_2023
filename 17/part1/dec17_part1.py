import os
import time
import functools
import sys

f = open(os.path.dirname(__file__) + '/../input.txt', 'r')
lines = [l.rstrip() for l in f.readlines()]

class Node:
    def __init__(self, value, x, y, d):
        self.x=x
        self.y=y
        self.value = value
        self.direction = d
        self.parent = None
    
    def setParent(self, parent):
        self.parent = parent
    def setValue(self, value):
        self.value = value
    def setDirection(self, direction):
        self.direction = direction
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return other.x==self.x and other.y==self.y
        return False
    def __str__(self):
        return f"({self.x} ; {self.y}) : {self.value} : {self.direction}"
    def __repr__(self):
        return f"({self.x} ; {self.y}) : {self.value} : {self.direction}"

def insertNodeInList(list, n):
    index = len(list)
    for i in range(len(list)):
      if list[i].value > n.value:
        index = i
        break
 
    if index == len(list):
      list = list[:index] + [n]
    else:
      list = list[:index] + [n] + list[index:]
    return list

def getNeighbors(node):
    x, y, v = node.x, node.y, node.value
    neighbors = []
    if x>0:
        neighbors.append(Node(v+int(lines[y][x-1]), x-1, y, node.direction+'l'))
    if x<len(lines[0])-1:
        neighbors.append(Node(v+int(lines[y][x+1]), x+1, y, node.direction+'r'))
    if y<len(lines)-1:
        neighbors.append(Node(v+int(lines[y+1][x]), x, y+1, node.direction+'d'))
    if y>0:
        neighbors.append(Node(v+int(lines[y-1][x]), x, y-1, node.direction+'u'))
    return neighbors

def AStar(objX, objY):
    openList = [Node(0,0,0,'')]
    closedList = []
    finalNode = None
    while len(openList) != 0:
        node = openList.pop(0)
        closedList.append(node)
        if node.x==objX and node.y==objY: # end case
            finalNode = node
            printPath(finalNode)
            break
        neighbors = getNeighbors(node)
        for n in neighbors:
            if n in closedList or n.direction[-4:] == n.direction[-1]*4:
                pass
            elif not n in openList:
                n.setParent(node)
                openList = insertNodeInList(openList, n)
            elif n in openList:
                otherNode = list(filter(lambda m: m.x==n.x and m.y==n.y, openList))[0]
                if otherNode.value > n.value:
                    otherNode.setValue(n.value)
                    otherNode.setParent(node.parent)
                    otherNode.setDirection(n.direction)
        openList = sorted(openList, key=functools.cmp_to_key(lambda a, b: a.value-b.value))
        #printPathValue(closedList)
        #time.sleep(0.1)

    if finalNode == None:
        raise Exception(f"No path found to go on {objX} ; {objY}")
    return finalNode, closedList

def printPath(node):
    nodes = [node]
    while node != None:
        print(f"{node.x},{node.y}", end=" -> ")
        nodes.append(node)
        node = node.parent
    print()

    for y in range(13):
        l=''
        for x in range(13):
            n = Node(None, x, y, None)
            if n in nodes:
                n = list(filter(lambda m: m.x==n.x and m.y==n.y, nodes))[0]
                if len(n.direction)==0:
                    l+='#'
                elif n.direction[-1]=='r':
                    l+='>'
                elif n.direction[-1]=='l':
                    l+='<'
                elif n.direction[-1]=='u':
                    l+='^'
                elif n.direction[-1]=='d':
                    l+='v'
            else:
                l+='.'
        print(l)

LINE_UP = '\033[1A'
LINE_CLEAR = '\x1b[2K'
def printPathValue(nodes):
    for y in range(13):
        l=''
        for x in range(13):
            n = Node(None, x, y, None)
            if n in nodes:
                n = list(filter(lambda m: m.x==n.x and m.y==n.y, nodes))[0]
                v = n.value
                v='00'+str(v) if v<10 else '0'+str(v) if v<100 else str(v)
                l+= v + ' '
            else:
                l+='... '
        sys.stdout.write(l+'\n')
    #print(LINE_UP*13, end=LINE_CLEAR)


def main():
    x, y = len(lines[0])-1, len(lines)-1
    node, closedList = AStar(x, y)
    print('\n'*2)
    printPathValue(closedList)
    printPath(node)
    return node

if __name__ == '__main__': 
    start = time.perf_counter()
    print(main())
    end = time.perf_counter()
    print(f"Executed in {((end - start)*1000):0.2f} milliseconds")