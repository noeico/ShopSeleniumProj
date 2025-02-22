from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from random import randint
from time import sleep

# Create a browser object (Open the browser)
driver = webdriver.Chrome()

# Go to the required URL
driver.get("https://juliemr.github.io/protractor-demo/")

# Maximize the window
driver.maximize_window()

# Define a timeout: In case an element is not found - wait 10 seconds
driver.implicitly_wait(10)

# Find Elements
num1 = driver.find_element(By.CSS_SELECTOR,"[ng-model='first']")
num2 = driver.find_element(By.CSS_SELECTOR,"[ng-model='second']")
operator = driver.find_element(By.CSS_SELECTOR,"[ng-model='operator']")
op_dropdown = Select(operator)  # Create a Select object (DropDown)
go = driver.find_element(By.ID,"gobutton")


# Perform 5 calculations
for i in range(5):
    num1_int = randint(1,100)
    num1.send_keys(str(num1_int))

    num2_int = randint(1, 100)
    num2.send_keys(str(num2_int))

    op_dropdown.select_by_visible_text("*")

    go.click()

    # Get the result
    result = driver.find_element(By.CSS_SELECTOR, "h2[class='ng-binding']")

    while result.text[0] == ".":
        pass

    # Get the history result
    top_history_result = driver.find_element(By.XPATH,"//tbody/tr[1]/td[3]")

    result_int = int(result.text)
    result_history_int = int(top_history_result.text)

    if result_int == num1_int * num2_int:
        print("test passed")
    else:
        print(f"test failed, result is {result_int}")

    if result_history_int == num1_int * num2_int:
        print("test passed")
    else:
        print(f"test failed, result in history is {result_history_int}")


# Print the history table

table = driver.find_element(By.CLASS_NAME,"table")

tr_s = table.find_elements(By.TAG_NAME,"tr")

th_s = tr_s[0].find_elements(By.TAG_NAME,"th")

# Print the header
for th in th_s:
    print(th.text, end="\t\t")

print()
# Print the data
for tr in tr_s[1:]:
    td_s = tr.find_elements(By.TAG_NAME,"td")
    for td in td_s:
        print(td.text, end="\t\t")
    print()

sleep(3)