#!/usr/bin/env python3

# Imports
import time
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



sel.select_by_visible_text("Florida")
time.sleep(1)
sel.select_by_visible_text("Texas")
time.sleep(1)

# Select a state
#sel.select_by_visible_text("California")

time.sleep(5)
