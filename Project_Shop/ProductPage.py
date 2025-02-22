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
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
import time


class ProductPage:
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver
        self.quantity = 0
        self.products_titles_list = []
        self.products_quantity_dict = {}  # each product will get its quantity
        self.products_prices_dict = {} # save price as shown on the page

    def product_title(self):
        return self.driver.find_element(By.CSS_SELECTOR,".page-title")

    def add_title_to_titles_list(self):
        return self.products_titles_list.append(self.product_title().text)

    def get_products_titles_list(self):
        return self.products_titles_list

    def insert_quantity_to_dict(self):
        self.products_quantity_dict[self.product_title().text] = self.get_the_selector_quantity()

    def get_quantity_dict(self):
        return self.products_quantity_dict

    def insert_price_to_dict(self):
        self.products_prices_dict[self.product_title().text] = self.get_unit_price()

    def update_price_dict(self):
        """saves the name of the product with its actual price of it"""
        self.products_prices_dict[self.product_title().text] = self.get_unit_price()

    def get_price_dict(self):
        return self.products_prices_dict

    def get_element_price(self):
        """if the element is not found then it tries 2 times more"""
        retries = 3  # try fo max 3 times
        for attempt in range(retries):
            try:
                element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".pd-price span"))
                )
                return element.text
            except StaleElementReferenceException:
                time.sleep(1) # wait 1 second and then try again
            except TimeoutException:
                return None

        raise Exception("Element unvailable")

    def get_unit_price(self):
        price_text = self.get_element_price()
        price = price_text.split()[0][1:]  # seperate the price from the text
        price = price.replace(",", "") # remove the ","
        price = float(price)
        return price

    def selector_quantity(self):
        return self.driver.find_element(By.CSS_SELECTOR,".form-control-lg")

    def update_selector_quantity(self, quantity):
        self.selector_quantity().clear()
        self.selector_quantity().click()
        self.selector_quantity().send_keys(quantity)

    def update_sum_of_quantities(self):
        """sum the total quantities from all the products together"""
        self.quantity += int(self.selector_quantity().get_attribute("value"))
        return self.quantity

    def get_the_selector_quantity(self):
        """return the quantity after the quantity has set"""
        return int(self.selector_quantity().get_attribute("value"))

    def get_sum_of_quantities(self):
        return self.quantity

    def list_of_quantities_elements_from_cart(self):
        return self.driver.find_elements(By.NAME, "item.EnteredQuantity")

    def calculate_quantities_from_cart(self):
        total = 0
        for product_quantity in self.list_of_quantities_elements_from_cart():
            total += int(product_quantity.get_attribute("value"))
        return total

    def add_to_cart_button(self):
        return self.driver.find_element(By.CSS_SELECTOR,".btn-add-to-cart")

    def click_add_to_cart(self):
        return self.add_to_cart_button().click()
















