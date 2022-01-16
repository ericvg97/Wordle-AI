from BrowserInteractor import BrowserInteractor
from EricStrategy import EricStrategy
from TerminalInteractor import TerminalInteractor
from Wordle import Wordle
from Words import words
import sys
from Player import Player

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'terminal':
        interactor = TerminalInteractor()
    else:
        interactor = BrowserInteractor()

    wordle = Wordle()
    strategy = EricStrategy(words, wordle)

    player = Player(words, interactor, strategy, wordle)
    player.play()
        
