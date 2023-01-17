#!/usr/bin/env python3

# Imports
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# Use the demo.seleniumeasy.com site with all of its practice pages
# 1. Input forms - Four checkboxs in "Multiple Checkbox Demo"
# at http://demo.seleniumeasy/basic-checkbox-demo.hmtl

driver =  webdriver.Chrome(service=Service(ChromeDriverManager().install()))  
driver.get("http://demo.seleniumeasy.com/basic-checkbox-demo.html")

# Select the "Check All" button and verify that all four checkboxes are checked
# id="check1"
id = "check1"  # define variable
button_id = driver.find_element(By.ID, id)


# Click on checkbox
button_id.click()

# Pause for 10 second to verify that the four checkboxes are now checked
time.sleep(10)


# Verify that the button name has changed to "Check All"
#print(dir(button_id))  #DEBUG
print(button_id.get_attribute("value"))  # This value should be "Uncheck All"

# Uniquely identify the four different checkboxes
box_1 = "//label[text() = 'Option 1']"
box_2 = "//label[text() = 'Option 2']"
box_3 = "//label[text() = 'Option 3']"
box_4 = "//label[text() = 'Option 4']"
time.sleep(1)
checkbox_1 = driver.find_element(By.XPATH, box_1)
checkbox_1.click()
time.sleep(1)
checkbox_2 = driver.find_element(By.XPATH, box_2)
checkbox_2.click()
time.sleep(1)
checkbox_3 = driver.find_element(By.XPATH, box_3)
checkbox_3.click()
time.sleep(1)
checkbox_4 = driver.find_element(By.XPATH, box_4)
checkbox_4.click()

time.sleep(10)
