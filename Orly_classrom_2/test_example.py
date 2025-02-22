from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Create a browser object (Open the browser)
driver = webdriver.Chrome()

# Go to the required URL
driver.get("https://www.advantageonlineshopping.com/#/")

# Maximize the window
driver.maximize_window()

# Define a timeout: In case an element is not found - wait 10 seconds
driver.implicitly_wait(10)

# Click on Speakers
#speakers = driver.find_element(By.CSS_SELECTOR, "#speakersImg")
#speakers = driver.find_element(By.ID, "speakersImg")
speakers = driver.find_element(By.CSS_SELECTOR, "[id='speakersImg']")
speakers.click()

# Click on a specific speaker
driver.find_element(By.ID, "25").click()

# Display the name and price of the product
#name_element = driver.find_element(By.CSS_SELECTOR,"h1.screen768")
#name_element = driver.find_element(By.CSS_SELECTOR,"h1[class='roboto-regular screen768 ng-binding']")
name_element = driver.find_element(By.CSS_SELECTOR,"#Description>h1")
print(f"product name: {name_element.text}")

#price_element = driver.find_element(By.CSS_SELECTOR,"h2.screen768:nth-child(2)")
price_element = driver.find_element(By.CSS_SELECTOR,"#Description>h2")
print(f"product price: {price_element.text}")

# Choose color
#red_color = driver.find_element(By.CSS_SELECTOR, "span[title='RED'][id='bunny']")
#red_color = driver.find_element(By.XPATH, "//span[@title='RED'][@id='bunny']")
red_color = driver.find_element(By.XPATH, "//*[@id='bunny'][4]")
red_color.click()

# Change quantity to 5
#quantity = driver.find_element(By.CSS_SELECTOR,"[name='quantity']")
quantity = driver.find_element(By.NAME,"quantity")
#quantity.clear()    Clear a text box. Not in this case because the field can't be empty.
quantity.send_keys(Keys.BACK_SPACE+"5")

# click on "Add to Cart"
driver.find_element(By.CSS_SELECTOR,"[name='save_to_cart']").click()

# Get the total from cart
cart_total = driver.find_element(By.CLASS_NAME,"cart-total")

# Wait for the cart total to be visible so we can "see" the text
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"cart-total")))

print("text",cart_total.text)
#print(cart_total.get_attribute("innerHTML"))

# Check that the cart total is calculated correctly
price = float(price_element.text[1:])
total = float(cart_total.text[1:])

if price*5 == total:
    print("test passed")
else:
    print(f"test failed! total is {total}")

sleep(5)
