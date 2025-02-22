from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://demo.guru99.com/test/newtours/")

driver.maximize_window()

driver.implicitly_wait(10)

driver.find_element(By.LINK_TEXT,"Flights").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Car").click()

redcolor = driver.find_element(By.XPATH,"//*[@id="bunny"]")

sleep(5)