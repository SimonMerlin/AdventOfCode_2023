import os
import operator
import time
from functools import reduce

f = open(os.path.dirname(__file__) + '/../input.txt', 'r')
lines = [l.rstrip() for l in f.readlines()]

def parseGame(game):
    gameDict = {}
    game = game.split(':')[1]
    rounds = [r.strip() for r in game.split(';')]
    for r in rounds:
        for dices in r.split(','):
            count, color = dices.strip().split(' ')
            if(color not in gameDict.keys()) or gameDict[color] < int(count):
                gameDict[color] = int(count)
    return gameDict

def multiplyDice(game):
    return reduce(operator.mul, [game[c] for c in game.keys()], 1)

def main():
    gamesPower = []
    for game in lines:
        gameParsed = parseGame(game)
        gamesPower.append(multiplyDice(gameParsed))
    return sum(gamesPower)

if __name__ == '__main__': 
    start = time.perf_counter()
    print(main())
    end = time.perf_counter()
    print(f"Executed in {((end - start)*1000):0.2f} milliseconds")