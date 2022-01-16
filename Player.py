from Interactor import Interactor
from Strategy import Strategy
from Wordle import Wordle
from typing import List


class Player():
    def __init__(self, words: List[str], interactor: Interactor, strategy: Strategy, wordle: Wordle):
        self.words = words
        self.interactor = interactor
        self.strategy = strategy
        self.wordle = wordle
    
    def play(self):
        found = False
        numTries = 0
        stillAvailable = self.words

        while not found and numTries < 6:
            tryWord = self.strategy.findBestWord(stillAvailable, numTries)

            rule = self.interactor.tryWord(tryWord, numTries)

            win = True
            for result in rule:
                if result.color != 'G':
                    win = False
                    break

            if win:
                print("Yuhuuu I won")
                break

            stillAvailable = self.wordle.findStillAvailable(rule, stillAvailable)

            numTries += 1