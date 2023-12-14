import os
import time

f = open(os.path.dirname(__file__) + '/../input.txt', 'r')
lines = [l.rstrip() for l in f.readlines()]

colorsMax = {'red': 12, 'green': 13, 'blue': 14}

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

def isPossible(game):
    return all([colorsMax[c] >= game[c] for c in game.keys()])

def main():
    counter = 0
    for game in lines:
        gameId = int(game.split(':')[0].split(" ")[1])
        gameParsed = parseGame(game)
        if isPossible(gameParsed):
            counter += gameId
    return counter

if __name__ == '__main__': 
    start = time.perf_counter()
    print(main())
    end = time.perf_counter()
    print(f"Executed in {((end - start)*1000):0.2f} milliseconds")