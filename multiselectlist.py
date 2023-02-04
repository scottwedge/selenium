#!/usr/bin/env python3

# Imports
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

# Work on the Select List Demo pulldown list (states)

# Use the demo.seleniumeasy.com site with all of its practice pages
# 1. Input forms - Radio buttons in Input Forms
# at http://demo.seleniumeasy/basic-select-dropdown-demo.html
web_site = "http://demo.seleniumeasy.com/basic-select-dropdown-demo.html"

driver =  webdriver.Chrome(service=Service(ChromeDriverManager().install()))  
driver.get(web_site)

# Select each of the values in the multi select list by index
name = "States"
sel = Select(driver.find_element(By.NAME, name))

# DEBUG
#print(dir(sel))  # options for sel
# 'all_selected_options', 'deselect_all', 'deselect_by_index', 
# 'deselect_by_value', 'deselect_by_visible_text', 'first_selected_option', 
# 'is_multiple', 'options', 'select_by_index', 'select_by_value', 
# 'select_by_visible_text']

# list of states in order:
# California, Florida, New Jersey, New York, Ohio, Texas, Pennsylvania, Washington
list_of_states = ["California", "Florida", "New Jersey", "New York", "Ohio", "Texas", "Pennsylvania", "Washington"]
length_of_list = len(list_of_states)
print("Length of states list",list_of_states, "is", length_of_list)


# Select random value from list
index = random.randint(0,length_of_list - 1)
print("Index =", index)

state = list_of_states[index]
print("Random state is", state)
sel.select_by_visible_text(state)

# sel.select_by_visible_text("Florida")
# time.sleep(1)
# sel.select_by_visible_text("Texas")
# time.sleep(1)

# Check the contents after select the "First Selected" button
first_selected_button_id = "printMe"
driver.find_element(By.ID, first_selected_button_id).click()


# Verify that the output text matches the selected state
output_class = "getall-selected"

#print(dir(driver))  #DEBUG
#print(dir(By))  #DEBUG


button_id = "//*[@class='getall-selected']"

result_text = driver.find_element(By.XPATH, button_id).text
print(result_text)

# Verify state in output text
if state in result_text:
    print("State", state, "is in text", result_text)
else:
    print("ERROR State", state, "is in text", result_text)


# Select second state and verify output is correct
# Select random value from list for second state
second_index = random.randint(0,length_of_list - 1)
print("Index =", second_index)
second_state = list_of_states[second_index]
print("Random state is", second_state)
sel.select_by_visible_text(second_state)


time.sleep(5)
