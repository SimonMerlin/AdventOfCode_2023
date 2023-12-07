import sys
import os
import time
from functools import reduce
import operator
import functools

f = open(os.path.join(sys.path[0], './../input.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

cardsOrder = "J23456789TQKA"
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
        self.originalCards = cards
    
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
    
    def replaceJ(self):
        if 'J' in self.cards:
            originalHands = self.cards
            maxHandOrder, newMaxHand = None, 0
            for c in cardsOrder:
                self.cards = originalHands.replace('J', c)
                if maxHandOrder==None or self.getHandOrder() > maxHandOrder:
                    maxHandOrder = self.getHandOrder()
                    newMaxHand = self.cards
            self.cards = newMaxHand
    
    def __str__(self):
        return "Hand {} ({}) : bid {} ; Value : {}".format(self.cards, self.originalCards, self.bid, self.getHandOrder())

def compareHands(hand1, hand2):
    hand1Value, hand2Value = hand1.getHandOrder(), hand2.getHandOrder()
    if hand1Value == hand2Value:
        index = [i for i in range(len(hand1.originalCards)) if hand1.originalCards[i]!=hand2.originalCards[i]][0]
        return cardsOrder.index(hand1.originalCards[index]) - cardsOrder.index(hand2.originalCards[index])
    return hand1Value - hand2Value


def main():
    hands = parseInput()
    for h in hands:
        h.replaceJ()
    hands = sorted(hands, key=functools.cmp_to_key(compareHands))
    return sum([h.bid*(hands.index(h)+1) for h in hands])

start = time.perf_counter()
print(main())
end = time.perf_counter()
print(f"Executed in {((end - start)*1000):0.2f} milliseconds")