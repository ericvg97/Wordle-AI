from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pyshadow.main import Shadow
from selenium.webdriver.common.action_chains import ActionChains
from Wordle import Rule

class BrowserInteractor:
    def tryWord(self, word, numTries):
        self.writeWord(word)
        return self.getRules(numTries)

    def closeInitialModal(self):
        element = self.shadow.find_element("section")
        element.click()

    def writeWord(self, word):
        actions = ActionChains(self.driver)
        actions.send_keys(word)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(3)

    def stringToRule(self, evaluation, letter):
        if evaluation == "absent":
            rule = Rule(letter, 'B')
        elif evaluation == "present":
            rule = Rule(letter, 'Y')
        else:
            rule = Rule(letter, 'G')
        
        return rule

    def getRules(self, row):
        element = self.shadow.find_elements("game-tile")

        rules = []
        for idx in range(row*5, row*5 + 5):
            evaluation = element[idx].get_attribute("evaluation")
            letter = element[idx].get_attribute("letter")
            

            rules += [self.stringToRule(evaluation, letter)]

        return rules

    def __init__(self):
        self.driver = webdriver.Chrome("./chromedriver")
        self.driver.get("https://www.powerlanguage.co.uk/wordle/")
        time.sleep(1)

        self.shadow = Shadow(self.driver)
        self.closeInitialModal()
    
    def __del__(self):
        print("dead")
        self.driver.close()

