from Interactor import Interactor
from typing import List
from Wordle import Rule

class TerminalInteractor(Interactor):
    def tryWord(self, word: str, numTries: int) -> List[Rule]:
        print('My next guess is:', word)
        return self.__parse(input("Enter rule (example i.B-n.B-u.B-l.Y-a.Y)\n"))

    def __parse(self, rulesText: str) -> List[Rule]:
        rulesSplit = rulesText.split('-')
        rules = []
        for rule in rulesSplit:
            component = rule.split('.')
            letter = component[0]
            color = component[1]
            rules += [Rule(letter, color)]

        return rules
