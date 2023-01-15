#!/usr/bin/env python3

# Imports
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# Use the demo.seleniumeasy.com site with all of its practice pages
# 1. Input forms - Simple checkbox at http://demo.seleniumeasy/basic-checkbox-demo.hmtl

driver =  webdriver.Chrome(service=Service(ChromeDriverManager().install()))  
driver.get("http://demo.seleniumeasy.com/basic-checkbox-demo.html")

# Search for id="isAgeSelected"
id = "isAgeSelected"  # define variable
checkbox_id = driver.find_element(By.ID, id)


# Click on checkbox
checkbox_id.click()

# Pause for 1 second
time.sleep(1)

# Verify that "success" statement is displayed
id = "txtAge"
success_message = "Success - Check box is checked"

success_element = driver.find_element(By.ID, id)
#success_element.text() == success_message

print("Success message is", success_element.text)
