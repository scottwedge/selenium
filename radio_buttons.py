#!/usr/bin/env python3

# Imports
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# Use the demo.seleniumeasy.com site with all of its practice pages
# 1. Input forms - Radio buttons in Input Forms
# at http://demo.seleniumeasy/basic-radiobutton-demo.html
web_site = "http://demo.seleniumeasy.com/basic-radiobutton-demo.html"

driver =  webdriver.Chrome(service=Service(ChromeDriverManager().install()))  
driver.get(web_site)

# Uniquely identify the two different radio buttons
male_button_id = "//*[@name='optradio' and @value='Male']"
female_button_id = "//*[@name='optradio' and @value='Female']"
radio_button_male = driver.find_element(By.XPATH, male_button_id)
radio_button_female = driver.find_element(By.XPATH, female_button_id)


# Uniquely identify the "Get Checked value" button
get_checked_value_button_id = "buttoncheck"
get_checked_value = driver.find_element(By.ID, get_checked_value_button_id)


# Select the Male radio button then select the "Get Checked value" button
#print(dir(radio_button_male))  # DEBUG

radio_button_male.click()
get_checked_value.click()

time.sleep(10)

# Select the Female radio button then select the "Get Checked value" button
radio_button_female.click()
get_checked_value.click()

time.sleep(10)
