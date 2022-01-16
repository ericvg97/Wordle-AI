import time

class Rule:
    def __init__(self, letter, color):
        self.letter = letter
        self.color = color

class Wordle:
    def __init__(self, allWords):
        self.allWords = allWords
    
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

    def parse(self, rulesText):
        rulesSplit = rulesText.split('-')
        rules = []
        for rule in rulesSplit:
            component = rule.split('.')
            letter = component[0]
            color = component[1]
            rules += [Rule(letter, color)]

        return rules
        
    def computeRule(self, targetWord, triedWord):
        rules = [[]] * 5

        lettersTargetWord = [0] * (ord('z') - ord('a') + 1)

        for letter in targetWord:
            lettersTargetWord[ord(letter) - ord('a')] += 1

        for idx, letter in enumerate(targetWord):
            if letter == triedWord[idx]:
                lettersTargetWord[ord(letter) - ord('a')] -= 1

                rules[idx] = triedWord[idx] + ".G"
        
        for idx, letter in enumerate(targetWord):
            if letter == triedWord[idx]:
                continue
            
            letterTried = triedWord[idx]

            if lettersTargetWord[ord(letterTried) - 97] > 0:
                lettersTargetWord[ord(letterTried) - 97] -= 1
                
                rules[idx] = letterTried + ".Y"
            
            else:
                rules[idx] = letterTried + ".B"

        return self.parse("-".join(rules))

    def findStillAvailable(self, rule, wereAvailable):
        stillAvailable = []
        for word in wereAvailable:
            if self.isValid(word, rule):
                stillAvailable += [word]

        return stillAvailable

    def findBestWord(self, stillAvailable):
        bestTotal = 100000000000
        bestWord = ""

        for idx, wordTried in enumerate(self.allWords):
            start = time.time()
            total = 0
            for wordTarget in stillAvailable:
                stillAvailableNow = self.findStillAvailable(self.computeRule(wordTarget, wordTried), stillAvailable)

                numAvailable = len(stillAvailableNow)
                total += numAvailable
                
                if total > bestTotal:
                    break

            if total < bestTotal:
                bestTotal = total
                bestWord = wordTried

            end = time.time()
            print("ETA: ", (end - start)*(len(self.allWords) - idx), len(stillAvailable))

        if bestTotal == len(stillAvailable):
            return stillAvailable[0]

        return bestWord
