from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
import pandas as pd
from Project_Shop.HomePage import HomePage
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class ShoppingCartPage:
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver

    def get_title(self):
        """Wait for the shopping cart title to appear and return its text."""
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='page-title']/h1"))
        )
        return self.driver.find_element(By.XPATH, "//div[@class='page-title']/h1").text

    def list_of_products(self):
        """return a list of all the products on cart page"""
        products_elements  = self.driver.find_elements(By.CSS_SELECTOR,".cart-item-link")
        products_list = [product.text for product in products_elements] # convert each element to text
        return products_list

    def list_of_units_price(self):
        """return the units prices"""
        # prices_elements contains also the subtotal prices
        prices_elements = self.driver.find_elements(By.CSS_SELECTOR,"div.cart-col.cart-col-price span.price")
        prices_elements = [product.text for product in prices_elements]
        prices = [float(price.replace("$", "").replace(",", "").split()[0]) for price in prices_elements]
        # removing the subtotal elements in the odd indexes
        unit_prices = prices[::2]
        return unit_prices

    def list_unit_subtotal(self):
        """return a list with the subtotal fora each product"""
        # prices_elements contains also the unit  prices
        prices_elements = self.driver.find_elements(By.CSS_SELECTOR, "div.cart-col.cart-col-price span.price")
        prices_elements = [product.text for product in prices_elements]
        prices = [float(price.replace("$", "").replace(",", "").split()[0]) for price in prices_elements]
        # removing the units elements in the even indexes
        subtotal_prices = prices[1::2]
        return subtotal_prices

    def list_quantity_per_product(self):
        """return a list of quantity per procudt as an integer"""
        wait = WebDriverWait(self.driver, 5)
        quantities_elements = wait.until(
        EC.presence_of_all_elements_located((By.XPATH, "//input[contains(@name, 'itemquantity')]")))
        quantities = [int(quantity.get_attribute("value")) for quantity in quantities_elements]
        return quantities

    def list_quantity_per_product_elements(self):
        """retutn a list of quantity per product as an element"""
        sleep(2)
        quantities_elements = self.driver.find_elements(By.XPATH, "//input[contains(@name, 'itemquantity')]")
        return quantities_elements

    def get_product_price_dict(self):
        """Return a dictionary with product names as keys and unit prices as values."""
        products = self.list_of_products()
        prices = self.list_of_units_price()
        return dict(zip(products, prices))

    def get_product_quantity_dict(self):
        """Return a dictionary with product names as keys and quantities as values."""
        products = self.list_of_products()
        quantities = self.list_quantity_per_product()
        return dict(zip(products, quantities))

    def get_subtotal(self):
        """get the subtotal without any shipping,taxes, or additional charges"""
        subtotals_elements = self.driver.find_elements(By.CSS_SELECTOR,".cart-summary-value")
        subtotal_text  = subtotals_elements[0].text.strip()
        subtotal_text = subtotal_text.replace(",", "").replace("$", "").strip()
        subtotal_text = subtotal_text.split()[0]
        subtotal_float = float(subtotal_text)
        return subtotal_float

    def set_quantity(self, index, quantity):
        quantities_elements = self.list_quantity_per_product_elements()
        quantity_element = quantities_elements[index]
        quantity_element.clear()
        quantity_element.send_keys(str(quantity))
        quantity_element.send_keys(Keys.TAB)

    def calc_subtotal(self):
        """calculate the sum of each product subtotal into to final subtotal(before tax,shipping, etc)"""
        total = 0
        for unit_subtotal in self.list_unit_subtotal():
            total += unit_subtotal
        return total





