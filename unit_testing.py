#!/usr/bin/env python3

# Imports
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# Functions
#def single_input_field(msg):
#    id = "user-message"
#    enter_message_box = driver.find_element(By.ID, id)

class TestWebPage(unittest.TestCase):
    def test_single_input_field(self):
        self.assertTrue(True)

# launch Chrome browser
driver =  webdriver.Chrome(service=Service(ChromeDriverManager().install()))

web_site = "https://demo.seleniumeasy.com/basic-first-form-demo.html"
driver.get(web_site)

print("unit testing")

