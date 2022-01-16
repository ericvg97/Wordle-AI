from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pyshadow.main import Shadow
from selenium.webdriver.common.action_chains import ActionChains
from Wordle import Rule
from Interactor import Interactor
from typing import List

class BrowserInteractor(Interactor):
    def __init__(self):
        self.driver = webdriver.Chrome("./chromedriver")
        self.driver.get("https://www.powerlanguage.co.uk/wordle/")
        time.sleep(1)

        self.shadow = Shadow(self.driver)
        self.__closeInitialModal()
    
        
    def __del__(self):
        self.driver.close()

    def tryWord(self, word: str, numTries: int) -> List[Rule]:
        self.__writeWord(word)
        return self.__getRules(numTries)

    def __closeInitialModal(self) -> None:
        element = self.shadow.find_element("section")
        element.click()

    def __writeWord(self, word: str) -> None:
        actions = ActionChains(self.driver)
        actions.send_keys(word)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(3)

    def __stringToRule(self, evaluation: str, letter: str) -> Rule:
        if evaluation == "absent":
            rule = Rule(letter, 'B')
        elif evaluation == "present":
            rule = Rule(letter, 'Y')
        else:
            rule = Rule(letter, 'G')
        
        return rule

    def __getRules(self, row: int) -> List[Rule]:
        element = self.shadow.find_elements("game-tile")

        rules = []
        for idx in range(row*5, row*5 + 5):
            evaluation = element[idx].get_attribute("evaluation")
            letter = element[idx].get_attribute("letter")
            

            rules += [self.__stringToRule(evaluation, letter)]

        return rules

