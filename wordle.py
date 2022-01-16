from words import words
import time

class Rule:
    def __init__(self, letter, color):
        self.letter = letter
        self.color = color


def isValid(word, rules):
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


def parse(rulesText):
    rulesSplit = rulesText.split('-')
    rules = []
    for rule in rulesSplit:
        component = rule.split('.')
        letter = component[0]
        color = component[1]
        rules += [Rule(letter, color)]

    return rules
        
def computeRule(targetWord, triedWord):
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

    return parse("-".join(rules))

def findStillAvailable(rules, wereAvailable):
    stillAvailable = []
    for word in wereAvailable:
        isStillValid = True
        for rule in rules:
            if not isValid(word, rule):
                isStillValid = False
        
        if isStillValid:
            stillAvailable += [word]

    return stillAvailable

def findBestWord(stillAvailable):
    bestTotal = 100000000000
    bestWord = ""

    for idx, wordTried in enumerate(words):
        start = time.time()
        total = 0
        for wordTarget in stillAvailable:
            stillAvailableNow = findStillAvailable([computeRule(wordTarget, wordTried)], stillAvailable)

            numAvailable = len(stillAvailableNow)
            total += numAvailable
            
            if total > bestTotal:
                break

        if total < bestTotal:
            bestTotal = total
            bestWord = wordTried

        end = time.time()
        print("ETA: ", (end - start)*(len(words) - idx), len(stillAvailable))

    if bestTotal == len(stillAvailable):
        return stillAvailable[0]

    return bestWord


if __name__ == '__main__':
    rules = [
        "i.B-n.B-u.B-l.Y-a.Y",
        "s.G-t.B-o.Y-r.Y-e.B"
    ]

    rulesParsed = []
    for rule in rules:
        rulesParsed += [parse(rule)]

    start = time.time()

    stillAvailable = findStillAvailable(rulesParsed, words)
        
    print(findBestWord(stillAvailable))

    print(stillAvailable)

    print(time.time() - start)

    while True:
        rule = [parse(input("Enter rule\n"))]
        
        stillAvailable = findStillAvailable(rule, stillAvailable)
        
        print(len(stillAvailable)) 
        print(findBestWord(stillAvailable))
        print(stillAvailable)       