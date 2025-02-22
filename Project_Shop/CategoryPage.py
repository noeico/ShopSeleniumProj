from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
import pandas as pd
from Project_Shop.HomePage import HomePage
from random import randint
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CategoryPage:
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver
        self.rand_numbers_list = []  # Contains the rand numbers to prevent the same products chosen twice

    def products_list(self):
        """return a list of the products in the current page"""
        return self.driver.find_elements(By.CSS_SELECTOR,".art-name a")

    def random_product(self):
        """rand a product from the product list"""
        rand_product_num = randint(0, len(self.products_list()) - 1)
        while rand_product_num in self.rand_numbers_list: # Preventing duplicate product selection
            rand_product_num = randint(0, len(self.products_list()) - 1)
        self.rand_numbers_list.append(rand_product_num)
        return self.products_list()[rand_product_num]

    def click_on_random_product(self):
        return self.random_product().click()

    def clear_random_list(self): # If the test changes category, reset the random list.
        return self.rand_numbers_list.clear()
    
    def random_product_name(self):
        """returns the name of the random product"""
        return self.random_product().text

    def get_category_title(self):
        title = self.driver.find_element(By.CSS_SELECTOR,".page-title h1.h3")
        return title.text

    def click_on_product_by_name(self, product_name):
        products = self.products_list()

        for product in products:
            if product.text == product_name:
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(product)
                )
                product.click()
                return




