from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

# Create a browser object (Open the browser)
driver = webdriver.Chrome()

# Go to the required URL
driver.get("https://juliemr.github.io/protractor-demo/")

# Maximize the window
driver.maximize_window()

# Define a timeout: In case an element is not found - wait 10 seconds
driver.implicitly_wait(10)

# Find elements: num1, num2, operator
num1 = driver.find_element(By.CSS_SELECTOR,"[ng-model='first']")
num2 = driver.find_element(By.CSS_SELECTOR,"[ng-model='second']")
#operator = driver.find_element(By.CSS_SELECTOR,"[ng-model='operator']")
#operator = driver.find_element(By.CLASS_NAME,"span1")
operator = driver.find_element(By.CSS_SELECTOR,".span1")

# Check that the numbers are empty before the calculation
num1_value = num1.get_attribute("value")
if num1_value == "":
    print("test passed")
else:
    print(f"test failed num1 contains {num1_value}")

num2_value = num2.get_attribute("value")
if num2_value == "":
    print("test passed")
else:
    print(f"test failed num2 contains {num2_value}")

# Check that the operator is + as default
op_value = operator.get_attribute("value")
if op_value == "ADDITION":
    print("test passed")
else:
    print(f"test failed operator contains {op_value}")

num1.send_keys("9")         # Type 9 in First number
num2.send_keys("5")         # Type 5 in Second number

# Create a Select object (DropDown)
op_dropdown = Select(operator)

op_dropdown.select_by_visible_text("*") # Choose operator: *

# Click Go
driver.find_element(By.ID,"gobutton").click()

# Get the result
#result = driver.find_element(By.CSS_SELECTOR,"h2[class='ng-binding']")
result = driver.find_element(By.CSS_SELECTOR,"h2.ng-binding")

# Wait for calculation to be done
while result.text[0]==".":
    pass

# Check that the numbers are empty after the calculation is done
num1_value = num1.get_attribute("value")
if num1_value == "":
    print("test passed")
else:
    print(f"test failed num1 contains {num1_value}")

num2_value = num2.get_attribute("value")
if num2_value == "":
    print("test passed")
else:
    print(f"test failed num2 contains {num2_value}")

# Check that the result is 45
if result.text == "45":
    print("test passed")
else:
    print(f"test failed, result is {result.text}")

sleep(3)