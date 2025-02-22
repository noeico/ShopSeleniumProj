from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

# Create a browser object (Open the browser)
driver = webdriver.Chrome()

# Go to the required URL
driver.get("https://demo.guru99.com/test/newtours/")

# Maximize the window
driver.maximize_window()

# Define a timeout: In case an element is not found - wait 10 seconds
driver.implicitly_wait(10)

driver.find_element(By.LINK_TEXT,"Flights").click()

driver.find_element(By.PARTIAL_LINK_TEXT,"Car").click()

sleep(3)