import time

class Rule:
    def __init__(self, letter, color):
        self.letter = letter
        self.color = color

class Wordle:    
    def isValid(self, word, rules):
        letters = [0] * (ord('z') - ord('a') + 1)
        for letter in word:
            letters[ord(letter) - ord('a')] += 1
        
        for idx, rule in enumerate(rules):
            if rule.color != 'G':
                continue

            if word[idx] != rule.letter:
                return False

            letters[ord(rule.letter) - ord('a')] -= 1
        
        for idx, rule in enumerate(rules):
            if rule.color == 'G':
                continue

            if rule.color == 'B':
                if letters[ord(rule.letter) - ord('a')] != 0:
                    return False
                
                continue
                        
            if letters[ord(rule.letter) - ord('a')] == 0 or word[idx] == rule.letter:
                return False

            letters[ord(rule.letter) - ord('a')] -= 1


        return True
        
    def computeRule(self, targetWord, triedWord):
        rules = [[]] * 5

        lettersTargetWord = [0] * (ord('z') - ord('a') + 1)

        for letter in targetWord:
            lettersTargetWord[ord(letter) - ord('a')] += 1

        for idx, letter in enumerate(targetWord):
            if letter == triedWord[idx]:
                lettersTargetWord[ord(letter) - ord('a')] -= 1

                rules[idx] = Rule(triedWord[idx], "G")
        
        for idx, letter in enumerate(targetWord):
            if letter == triedWord[idx]:
                continue
            
            letterTried = triedWord[idx]

            if lettersTargetWord[ord(letterTried) - 97] > 0:
                lettersTargetWord[ord(letterTried) - 97] -= 1
                
                rules[idx] = Rule(letterTried, "Y")
            
            else:
                rules[idx] = Rule(letterTried, "B")

        return rules

    def findStillAvailable(self, rule, wereAvailable):
        stillAvailable = []
        for word in wereAvailable:
            if self.isValid(word, rule):
                stillAvailable += [word]

        return stillAvailable
