import os
import time

f = open(os.path.dirname(__file__) + '/../input.txt', 'r')
lines = [l.rstrip() for l in f.readlines()]

def parseCard(id, card):
    winningNumbers, myNumbers = card.split(':')[1].split('|')
    winningNumbers = [int(n.strip()) for n in winningNumbers.split(' ') if n != '']
    myNumbers = [int(n.strip()) for n in myNumbers.split(' ') if n != '']
    return Card(id, winningNumbers, myNumbers)

class Card:
    def __init__(self, id, winningNumbers, myNumbers):
        self.id = id
        self.count = 1
        self.matchingCount = len(set(winningNumbers).intersection(set(myNumbers)))
    
    def increment(self, incr):
        self.count += incr
    
    def __str__(self):
        return "Card #{} : count {}".format(self.id, self.count, self.matchingCount)
    

def main():
    cards = {}
    for i in range(len(lines)):
        cards[i+1] = parseCard(i, lines[i])

    for i in range(1, len(lines)+1):
        c = cards[i]
        for j in range(i+1, i+c.matchingCount+1):
            if j<len(lines):
                cards[j].increment(c.count)

    return sum(v.count for k, v in cards.items())

if __name__ == '__main__': 
    start = time.perf_counter()
    print(main())
    end = time.perf_counter()
    print(f"Executed in {((end - start)*1000):0.2f} milliseconds")