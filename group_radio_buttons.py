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

# Work on the Group Radio Buttons Demo section
# Uniquely identify the two different Sex radio buttons
male_button_id = "//*[@name='gender' and @value='Male']"
female_button_id = "//*[@name='gender' and @value='Female']"
radio_button_male = driver.find_element(By.XPATH, male_button_id)
radio_button_female = driver.find_element(By.XPATH, female_button_id)

# Uniquely identify the three Age group radio buttons
age_group_0_to_5_id = "//*[@name='ageGroup' and @value='0 - 5']"
age_group_5_to_15_id = "//*[@name='ageGroup' and @value='5 - 15']"
age_group_15_to_50_id = "//*[@name='ageGroup' and @value='15 - 50']"
age_button_0_to_5 = driver.find_element(By.XPATH, age_group_0_to_5_id)
age_button_5_to_15 = driver.find_element(By.XPATH, age_group_5_to_15_id)
age_button_15_to_50 = driver.find_element(By.XPATH, age_group_15_to_50_id)

# "Uniquely identify the "Get values" button
get_values_button_id = "//*[@type='button' and text()='Get values']"
get_values_button = driver.find_element(By.XPATH, get_values_button_id)


# Select the Male radio button 
radio_button_male.click()


# Select the "0 to 5" Age Group button
age_button_0_to_5.click()

# Select the "Get values" button
get_values_button.click()

time.sleep(10)

# Check output is correct
result = driver.find_element(By.CLASS_NAME, "groupradiobutton")
print(result)
print(result.text)

time.sleep(10)

