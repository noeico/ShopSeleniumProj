from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Create a browser object (Open the browser)
driver = webdriver.Chrome()

# Go to the required URL
driver.get("https://juliemr.github.io/protractor-demo/")

# Maximize the window
driver.maximize_window()

# Define a timeout: In case an element is not found - wait 10 seconds
driver.implicitly_wait(10)

# Type 9 in First number
num1 = driver.find_element(By.CSS_SELECTOR,"[ng-model='first']")
num1.send_keys("9")
#print("text", num1.get_attribute("value"))

# Type 5 in Second number
num2 = driver.find_element(By.CSS_SELECTOR,"[ng-model='second']")
num2.send_keys("5")

# Find the operator element
operator = driver.find_element(By.CSS_SELECTOR,"[ng-model='operator']")

# Create a Select object (DropDown)
op_dropdown = Select(operator)

# Choose operator: *
op_dropdown.select_by_visible_text("*")

# Click Go
driver.find_element(By.ID,"gobutton").click()

# Wait for calculation to be done
wait = WebDriverWait(driver, 10)
#wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"td[class='ng-binding']")))
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"td.ng-binding")))

# Get the result
result = driver.find_element(By.CSS_SELECTOR,"h2.ng-binding")

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