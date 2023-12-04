import sys
import os
import operator
import time
from functools import reduce
f = open(os.path.join(sys.path[0], './../input.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

def parseGame(game):
    gameDict = {}
    game = game.split(':')[1]
    rounds = [r.strip() for r in game.split(';')]
    for r in rounds:
        for dices in r.split(','):
            d = dices.strip().split(' ')
            if(d[1] not in gameDict.keys()) or gameDict[d[1]] < int(d[0]):
                gameDict[d[1]] = int(d[0])
    return gameDict

def multiplyDice(game):
    return reduce(operator.mul, [game[c] for c in game.keys()], 1)

def main():
    gamesPower = []
    for game in lines:
        gameParsed = parseGame(game)
        gamesPower.append(multiplyDice(gameParsed))
    return sum(gamesPower)

start = time.perf_counter()
print(main())
end = time.perf_counter()
print(f"Executed in {((end - start)*1000):0.2f} milliseconds")