import sys
import os
f = open(os.path.join(sys.path[0], './../data.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

colorsMax = {'red': 12, 'green': 13, 'blue': 14}

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

def isPossible(game):
    return all([colorsMax[c] >= game[c] for c in game.keys()])

counter = 0
for game in lines:
    gameId = int(game.split(':')[0].split(" ")[1])
    gameParsed = parseGame(game)
    if isPossible(gameParsed):
        counter += gameId
print(counter)