#!/usr/bin/env python3

# Imports
from selenium import webdriver
# according to https://stackoverflow.com/questions/64717302/deprecationwarning-executable-path-has-been-deprecated-selenium-python
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# from https://www.youtube.com/watch?v=kpONBQ3muLg
#from selenium.webdriver.firefox.service import Service
#from selenium.webdriver.firefox.options import Options

# launch Chrome browser
driver =  webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")

print(driver.title)  # Get and print window title
driver.close()


# select second web site
driver =  webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # Must repeat driver setting else fails here
driver.get("https://techwithtim.net")
print(driver.title)
driver.quit()


# configureFirefox web browser
#user_agent = 
#firefox_driver = 
#firefox_service = 
#firefox_options =

# launch Firefox web browser
#driver = webdriver.Firefox()
#driver.get("https://techwithtim.net")
#print(driver.title)
#driver.close()
