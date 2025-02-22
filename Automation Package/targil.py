from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://juliemr.github.io/protractor-demo/")

driver.maximize_window()

driver.implicitly_wait(10)

num1 = driver.find_element(By.CSS_SELECTOR,"[ng-model='first']")
num1.send_keys("9")
num2 = driver.find_element(By.CSS_SELECTOR,"[ng-model='second']")
num2.send_keys("5")

#find the operator element
operator = driver.find_element(By.CSS_SELECTOR,"[ng-model='operator']")

#create a select object
op_dropdown = Select(operator)

#choose operator
op_dropdown.select_by_visible_text("*")

# Go button
driver.find_element(By.ID,"gobutton").click()

result = driver.find_element(By.CSS_SELECTOR,"h2.ng-binding")
while result.text[0]==".":
    pass

sleep(5)