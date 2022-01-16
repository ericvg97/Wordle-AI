from BrowserInteractor import BrowserInteractor
from EricStrategy import EricStrategy
from TerminalInteractor import TerminalInteractor
from Wordle import Wordle
from Words import words

if __name__ == '__main__':
    interactor = BrowserInteractor()
    # interactor = TerminalInteractor()

    found = False
    numTries = 0
    wordle = Wordle()
    strategy = EricStrategy(words, wordle)
    stillAvailable = words

    while not found and numTries < 6:
        tryWord = strategy.findBestWord(stillAvailable, numTries)

        rule = interactor.tryWord(tryWord, numTries)

        win = True
        for result in rule:
            if result.color != 'G':
                win = False
                break

        if win:
            print("Yuhuuu I won")
            break

        stillAvailable = wordle.findStillAvailable(rule, stillAvailable)

        numTries += 1
        
