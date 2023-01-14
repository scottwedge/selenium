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

# Search for id="sum1" and "sum2"
sum1_id = driver.find_element(By.ID, "sum1")
sum2_id = driver.find_element(By.ID, "sum2")

#  Use variables for entered data
val1 = 5
val2 = 6

# Enter text into the element using ".send_keys" 
sum1_id.send_keys(val1)
sum2_id.send_keys(val2)
time.sleep(5)  # Pause so can examine if textbox has entered values


# Need to select button with text label of "Get Total"
# NEW: Use relative xpath and search by Xpath
# NEW: ".click()" to press the button element

get_total_button_xpath = '//*[@type="button" and @onclick = "return total()"]'  # 

get_total_button = driver.find_element(By.XPATH, get_total_button_xpath)
get_total_button.click()  # Click on the button
time.sleep(5)  # Pause so can examine if click has caused value to be displayed


# Get result sum
sum_element = driver.find_element(By.ID, "displayvalue")
#print("Sum=", sum)  #DEBUG
#print("dir", dir(sum))  #DEBUG
print("Text of sum of values = ", sum_element.text)


