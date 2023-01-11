#!/usr/bin/env python3

# Imports
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# according to https://stackoverflow.com/questions/64717302/deprecationwarning-executable-path-has-been-deprecated-selenium-python
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# Use the demo.seleniumeasy.com site with all of its practice pages
# 1. Input forms - Simple Demo form at basic-first-form-demo.html
# NEW: search for element with "id" using "By.ID"
# NEW: print current time using "time.asctime()"
# NEW: enter text into found text box element using text_box_element.send_keys("text-goes-here")

driver =  webdriver.Chrome(service=Service(ChromeDriverManager().install()))  
driver.get("http://demo.seleniumeasy.com/basic-first-form-demo.html")

# Search for id="user-message"
element_by_id = driver.find_element(By.ID, "user-message")
print("Found element for 'id='user-message''=", element_by_id)

# Enter text into the element using ".send_keys" 
element_by_id.send_keys("Hello there. The time is: ", time.asctime())
time.sleep(10)  # Pause so can examine if textbox has entered values


# Need to select button with text label of "Show Message"
#show_message_button = driver.find_element(By.TYPE, "button")
show_message_button.click()  # Then click on the button
time.sleep(10)  # Pause so can examine if click has caused value to be displayed

