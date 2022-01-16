from BrowserInteractor import BrowserInteractor
from TerminalInteractor import TerminalInteractor
from Wordle import Wordle
from words import words

if __name__ == '__main__':
    interactor = BrowserInteractor()
    # interactor = TerminalInteractor()

    found = False
    numTries = 0
    wordle = Wordle()
    stillAvailable = words

    while not found and numTries < 6:
        if numTries == 0:
            tryWord = 'inula'
        elif numTries == 1:
            tryWord = 'store'
        else:
            tryWord = wordle.findBestWord(stillAvailable)

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
        
