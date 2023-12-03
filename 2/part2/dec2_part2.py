import sys
import os
import operator
from functools import reduce
f = open(os.path.join(sys.path[0], './../data.txt'), 'r')
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

gamesPower = []
for game in lines:
    gameId = int(game.split(':')[0].split(" ")[1])
    gameParsed = parseGame(game)
    gamesPower.append(multiplyDice(gameParsed))
print(sum(gamesPower))
