#!/usr/bin/env python3

# Imports
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# Use the demo.seleniumeasy.com site with all of its practice pages
# 1. Input forms - Simple Demo form at basic-first-form-demo.html

driver =  webdriver.Chrome(service=Service(ChromeDriverManager().install()))  
driver.get("http://demo.seleniumeasy.com/basic-first-form-demo.html")

# Search for id="user-message"
element_by_id = driver.find_element(By.ID, "user-message")
#print("Found element for 'id='user-message''=", element_by_id)

# Enter text into the element using ".send_keys" 
element_by_id.send_keys("Hello there. The time is: ", time.asctime())
time.sleep(5)  # Pause so can examine if textbox has entered values


# Need to select button with text label of "Show Message"
# NEW: Use relative xpath and search by Xpath
# NEW: ".click()" to press the button element

xpath_1 = '//button[@class="btn btn-default"]'  # This selects the first of two buttons
xpath_2 = '//*[@type="button" and @onclick="showInput();"]'  # This only selects the first button

show_message_button = driver.find_element(By.XPATH, xpath_1)
show_message_button.click()  # Then click on the button
time.sleep(5)  # Pause so can examine if click has caused value to be displayed


# Create known text string then verify that it is displayed (instead of always changing time)
known_text_string = "Match this string 123"

# re-use element with id="user-message" after clear field
element_by_id.clear()
# Enter text into the element using ".send_keys" 
element_by_id.send_keys(known_text_string)
time.sleep(5)  # Pause so can examine if textbox has entered values


# Use xpath_2 path
show_message_button = driver.find_element(By.XPATH, xpath_2)
show_message_button.click()  # Then click on the button
time.sleep(5)  # Pause so can examine if click has caused value to be displayed


# Then verify that the enter text is actually displayed
element_by_id_2 = driver.find_element(By.ID, "display")

print("This is element: ", element_by_id_2)
time.sleep(5)  # Pause so can examine if click has caused value to be displayed

# NEW: element.text to display text value of element
print(element_by_id_2.text)

