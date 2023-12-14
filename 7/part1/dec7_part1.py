import os
import time
from functools import reduce
import operator
import functools

f = open(os.path.dirname(__file__) + '/../input.txt', 'r')
lines = [l.rstrip() for l in f.readlines()]

cardsOrder = "23456789TJQKA"
handsValueOrder = [1, 2, 4, 3, 6, 4, 5]
                    
def parseInput():
    hands = []
    for hand in lines:
        h, bid = hand.split(' ')
        hands.append(Hand(h, int(bid)))
    return hands

class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid
    
    def getHandOrder(self):
        cardsCount = dict()
        for c in set([*self.cards]):
            cardsCount[c] = self.cards.count(c)
        handValue = reduce(operator.mul, cardsCount.values(), 1)

        if handValue != 4 :
            return handsValueOrder.index(handValue)
        else:
            if len(cardsCount.keys()) == 2:
                return 5
            return 2
        
    def __str__(self):
        return "Hand {} ({}) : bid {} ; Value : {}".format(self.cards, self.originalCards, self.bid, self.getHandOrder())

def compareHands(hand1, hand2):
    hand1Value, hand2Value = hand1.getHandOrder(), hand2.getHandOrder()
    if hand1Value == hand2Value:
        index = [i for i in range(len(hand1.cards)) if hand1.cards[i]!=hand2.cards[i]][0]
        return cardsOrder.index(hand1.cards[index]) - cardsOrder.index(hand2.cards[index])
    return hand1Value - hand2Value

def main():
    hands = sorted(parseInput(), key=functools.cmp_to_key(compareHands))
    return sum([h.bid*(hands.index(h)+1) for h in hands])

if __name__ == '__main__': 
    start = time.perf_counter()
    print(main())
    end = time.perf_counter()
    print(f"Executed in {((end - start)*1000):0.2f} milliseconds")