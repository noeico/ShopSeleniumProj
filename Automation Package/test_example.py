from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://www.advantageonlineshopping.com/#/")

driver.maximize_window()

driver.implicitly_wait(10)

# click on speakers category
#speakers = driver.find_element(By.CSS_SELECTOR, "#speakersImg")
speakers = driver.find_element(By.ID, "speakersImg")
speakers.click()

# click on specific speaker
# driver.find_element(By.CSS_SELECTOR,r"#\32 5").click()
driver.find_element(By.ID,"25").click()

#click on the red color
driver.find_element(By.CSS_SELECTOR,"[title='RED'][id=bunny]").click()

#change quantity to 15
quantity = driver.find_element(By.CSS_SELECTOR, "[name='quantity']")
#quantity.clear()
quantity.send_keys(Keys.BACKSPACE+"5")

#add to cart
driver.find_element(By.CSS_SELECTOR,"[name='save_to_cart']").click()

#wait = WebDriverWait(driver,10)
#waituntil

#show the name and the price of the product
name_element = driver.find_element(By.CSS_SELECTOR,"#Description>h1")
price_element = driver.find_element(By.CSS_SELECTOR,"h2.screen768:nth-child(2)")
print(f"Product is: {name_element.text}")
print(f"The price is: {price_element.text}")


sleep(5)