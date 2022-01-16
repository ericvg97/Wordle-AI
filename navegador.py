from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyshadow.main import Shadow
from selenium.webdriver.common.action_chains import ActionChains
from wordle import Rule
from wordle import findStillAvailable
from wordle import findBestWord
from words import words

def closeInitialModal(shadow):
    element = shadow.find_element("section")
    element.click()

def writeWord(word, driver):
    actions = ActionChains(driver)
    actions.send_keys(word)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    time.sleep(3)

def stringToRule(evaluation, letter):
    if evaluation == "absent":
        rule = Rule(letter, 'B')
    elif evaluation == "present":
        rule = Rule(letter, 'Y')
    else:
        rule = Rule(letter, 'G')
    
    return rule

def getInfo(row, shadow):
    element = shadow.find_elements("game-tile")

    rules = []
    for idx in range(row*5, row*5 + 5):
        evaluation = element[idx].get_attribute("evaluation")
        letter = element[idx].get_attribute("letter")
        

        rules += [stringToRule(evaluation, letter)]

    return rules

driver = webdriver.Chrome("./chromedriver")
driver.get("https://www.powerlanguage.co.uk/wordle/")
time.sleep(1)


shadow = Shadow(driver)
closeInitialModal(shadow)

writeWord('inula', driver)
rules = [getInfo(0, shadow)]

writeWord('store', driver)
rules += [getInfo(1, shadow)]

stillAvailable = findStillAvailable(rules, words)
word = findBestWord(stillAvailable)

writeWord(word, driver)



# time.sleep(3)
# driver.quit()

