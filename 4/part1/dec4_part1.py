import os
import time

f = open(os.path.dirname(__file__) + '/../input.txt', 'r')
lines = [l.rstrip() for l in f.readlines()]

def parseCard(card):
    winningNumbers, myNumbers = card.split(':')[1].split('|')
    winningNumbers = [int(n.strip()) for n in winningNumbers.split(' ') if n != '']
    myNumbers = [int(n.strip()) for n in myNumbers.split(' ') if n != '']
    return winningNumbers, myNumbers

def main():
    totalPoints = 0
    for card in lines:
        points = 0
        winningNumbers, myNumbers = parseCard(card)
        for n in myNumbers:
            if n in winningNumbers and points==0:
                points=1
            elif n in winningNumbers:
                points *= 2
        totalPoints += points
    return totalPoints

if __name__ == '__main__': 
    start = time.perf_counter()
    print(main())
    end = time.perf_counter()
    print(f"Executed in {((end - start)*1000):0.2f} milliseconds")