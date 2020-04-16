#! python3
# cmdEmailer.py - using selenium, send an email of the string to the provided address

import sys, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

recipient = sys.argv[1]
subject = sys.argv[2]
message = sys.argv[3]

# Username Login
browser = webdriver.Firefox()
browser.get('https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin')
idElem = browser.find_element_by_name('identifier')
idElem.send_keys('email@gmail.com')
idElem(Keys.ENTER)
time.sleep(3)

# Password Login
passElem = browser.find_element_by_name('password')
passElem.send_keys('password')
passElem.send_keys(Keys.ENTER)
time.sleep(5)

# Click Compose
composeElem = browser.find_element_by_name('z0')
composeElem.click()
time.sleep(5)

# Recipient
toElem = browser.find_element_by_name('to')
toElem.send_keys(recipient)

# Subject
subjectElem = browser.find_element_by_name('subjectbox')
subjectElem.send_keys(subject)

# Message
subjectElem.send_keys(Keys.TAB + message + Keys.TAB + Keys.ENTER)
time.sleep(5)

browser.quit()

