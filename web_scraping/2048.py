#! python3
# 2048.py - game to send up, right, down and left arrow keys to the 2048 game. Automatically plays the game for you

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')
htmlElem = browser.find_element_by_tag_name('html')

while True:
    htmlElem.send_keys(Keys.UP)
    htmlElem.send_keys(Keys.RIGHT)
    htmlElem.send_keys(Keys.DOWN)
    htmlElem.send_keys(Keys.LEFT)

