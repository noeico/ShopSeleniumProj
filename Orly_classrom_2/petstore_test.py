from selenium import webdriver
from selenium.webdriver.common.by import By
from random import randint, choice
from time import sleep

# Create a browser object (Open the browser)
driver = webdriver.Chrome()

# Go to the required URL
driver.get("https://petstore.octoperf.com/actions/Catalog.action")

# Maximize the window
driver.maximize_window()

# Define a timeout: In case an element is not found - wait 10 seconds
driver.implicitly_wait(10)

# Get pets categories list
pets_list = driver.find_elements(By.CSS_SELECTOR,"#SidebarContent>a")

# choice(pets_list).click()
#
pets_list[1].click()

# Find the Poodle and click on it

table = driver.find_element(By.TAG_NAME,"table")
tr_s = table.find_elements(By.TAG_NAME,"tr")

for tr in tr_s[1:]:
    td_s = tr.find_elements(By.TAG_NAME, "td")
    if td_s[1].text == "Poodle":
        td_s[0].click()
        break

# dogs = driver.find_element(By.XPATH,"//*[@id='SidebarContent']/a[2]")
# dogs.click()

sleep(2)