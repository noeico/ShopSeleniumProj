from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://juliemr.github.io/protractor-demo/")

#find the left and right fields - num1 and num2
num1 = driver.find_element(By.CSS_SELECTOR,"[ng-model='first']")
num1.send_keys("9")
num2 = driver.find_element(By.CSS_SELECTOR,"[ng-model='second']")
num2.send_keys("5")
driver.maximize_window()

#find the operator element
operator = driver.find_element(By.CSS_SELECTOR,"[ng-model='operator']")

#create a select object
op_dropdown = Select(operator)

#choose operator
op_dropdown.select_by_visible_text("*")

# Go button
driver.find_element(By.ID,"gobutton").click()

#check that the numbers fields are empty after the calc is done

operator = driver.find_element(By.CLASS_NAME,"span1")
driver.implicitly_wait(10)
sleep(5)