#!/usr/bin/env python3

# Imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# according to https://stackoverflow.com/questions/64717302/deprecationwarning-executable-path-has-been-deprecated-selenium-python


#
driver =  webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")

