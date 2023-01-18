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

# Uniquely identify the four different checkboxes
box_1 = "//label[text() = 'Option 1']"
box_2 = "//label[text() = 'Option 2']"
box_3 = "//label[text() = 'Option 3']"
box_4 = "//label[text() = 'Option 4']"
checkbox_1 = driver.find_element(By.XPATH, box_1)
checkbox_2 = driver.find_element(By.XPATH, box_2)
checkbox_3 = driver.find_element(By.XPATH, box_3)
checkbox_4 = driver.find_element(By.XPATH, box_4)


# Uniquely identify the button
# id="check1"
id = "check1"  # define variable
button_id = driver.find_element(By.ID, id)

# Verify that initially all four boxes are not checked and button label = "Check All"
if checkbox_1.is_selected():
    print("First checkbox is selected")
else:
    print("First checkbox is NOT selected")

if checkbox_2.is_selected():
    print("Second checkbox is selected")
else:
    print("Second checkbox is NOT selected")

if checkbox_3.is_selected():
    print("Third checkbox is selected")
else:
    print("Third checkbox is NOT selected")

if checkbox_4.is_selected():
    print("Fourth checkbox is selected")
else:
    print("Fourth checkbox is NOT selected")

if button_id.get_attribute("value") == "Check All":
    print("Button shows 'Check All'") 
else:
    print("Button does NOT show 'Check All'") 

time.sleep(10)

# Click on "check All" button and verify that:
# 1. the button name changes and 
# 2. all four check boxes are now checked
button_id.click()


# Verify that the button name has changed to "Uncheck All"
button_name = button_id.get_attribute("value")  # This value should be "Uncheck All"
if button_name == "Uncheck All":
    print("The button name has correctly changed to:", button_name)
else:
    print("The button name is now:", button_name)
 
# Check that all four checkboxes are now selected

if checkbox_1.is_selected() and checkbox_2.is_selected() and checkbox_3.is_selected() and checkbox_4.is_selected():
    print("All four checkboxes are selected")

# Click on each of four checkboxes to uncheck it
checkbox_1.click()
time.sleep(1)
checkbox_2.click()
time.sleep(1)
checkbox_3.click()
time.sleep(1)
checkbox_4.click()
time.sleep(1)

time.sleep(10)
