#!/usr/bin/env python3

# Imports
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# according to https://stackoverflow.com/questions/64717302/deprecationwarning-executable-path-has-been-deprecated-selenium-python
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# from https://www.youtube.com/watch?v=kpONBQ3muLg
#from selenium.webdriver.firefox.service import Service
#from selenium.webdriver.firefox.options import Options

# launch Chrome browser
driver =  webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")

print(driver.title)  # Current window title
print(driver.current_url)  # Current URL
driver.close()


# select second web site
driver =  webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # Must repeat driver setting else fails here
driver.get("https://techwithtim.net")
print(driver.title)  # Current window title
print(driver.current_url)  # Current URL

search_string = "Tutorials"  # Define string to search for
src = driver.page_source  # Capture all page source
print("Search string found in page source = ",search_string in src)  # Booleans result if search string found in page
driver.quit()


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
element_by_id.send_keys("Hello there. The time is: ", time.asctime())
time.sleep(10)  # Pause so can examine if textbox has entered values

