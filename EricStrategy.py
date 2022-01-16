from Strategy import Strategy
from typing import List
import time
from Wordle import Wordle

class EricStrategy(Strategy):
    def __init__(self, allWords: str, wordle: Wordle):
        self.allWords = allWords
        self.wordle = wordle

    def findBestWord(self, stillAvailable: List[str], numTries: int) -> str:
        if numTries == 0:
            return 'inula'
        elif numTries == 1:
            return 'store'

        bestTotal = 100000000000
        bestWord = ""

        start = time.time()

        for idx, wordTried in enumerate(self.allWords):
            total = 0
            for wordTarget in stillAvailable:
                stillAvailableNow = self.wordle.findStillAvailable(self.wordle.computeRule(wordTarget, wordTried), stillAvailable)

                numAvailable = len(stillAvailableNow)
                total += numAvailable
                
                if total > bestTotal:
                    break

            if total < bestTotal:
                bestTotal = total
                bestWord = wordTried

            now = time.time()
            print(idx, "/", len(self.allWords), "ETA: ", ((now - start)/(idx+1))*(len(self.allWords) - idx), len(stillAvailable))

        if bestTotal == len(stillAvailable):
            return stillAvailable[0]

        return bestWord