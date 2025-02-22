from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
import pandas as pd
from Project_Shop.HomePage import HomePage
from random import randint
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re


class CartSidebar:
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver

    def cart_products_names(self):
        """return a list of all the products in the cart"""
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".name.font-weight-medium"))
        )
        return self.driver.find_elements(By.CSS_SELECTOR, ".name.font-weight-medium")

    def cart_items(self):
        """Returns a list of all product elements in the cart"""
        return self.driver.find_elements(By.CSS_SELECTOR, ".offcanvas-cart-item")

    def bin_buttons(self):
        """returns list of all the bin buttons"""
        return self.driver.find_elements(By.CSS_SELECTOR, ".remove.ajax-cart-link")

    def go_to_cart_button(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-success")))

    def click_go_to_cart(self):
        return self.go_to_cart_button().click()

    def is_cart_sidebar_open(self):
        """check if the sidebar open"""
        try:
            return WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".offcanvas-cart-body.offcanvas-scrollable"))
            )
        except:
            return False

    def is_cart_sidebar_closed(self):
        """Check if the sidebar is closed"""
        try:
            return WebDriverWait(self.driver, 5).until(
                EC.invisibility_of_element_located((By.CSS_SELECTOR, ".offcanvas-cart-body.offcanvas-scrollable"))
            ) is True  # return true if the element disapeard
        except:
            return False  #if after 5 seconds the sidebar is on it return false

    def click_outside_cart_sidebar(self):
        return self.driver.find_element(By.TAG_NAME, "body").click()

    def get_cart_items(self):
        cart_items = self.driver.find_elements(By.CLASS_NAME, "offcanvas-cart-item")
        return cart_items

    def get_items_price_dict(self):
        """return a dictionary with key as prodcut_name and value as price"""
        cart_items = self.get_cart_items()
        prices = {}
        for item in cart_items:
            product_name = item.find_element(By.CSS_SELECTOR, ".name.font-weight-medium").text
            price_text = item.find_element(By.CSS_SELECTOR, ".price.unit-price").text
            price_value = re.sub(r"[^\d.]", "", price_text) # removes any commas, spaces and symbols
            price_value = float(price_value)
            prices[product_name] = price_value
        return prices

    def get_total_price_text(self):
        """return the subtotal price as it showen as text"""
        sub_total_text = self.driver.find_element(By.CSS_SELECTOR, ".sub-total.price").text
        return sub_total_text

    def get_total_price_float(self):
        """return the subtotal as float without any text, commas and symbols"""
        subtotal_with_text = self.get_total_price_text()
        subtotal_float = subtotal_with_text.split()[0][1:] # seperate the number from the rest
        subtotal_float = subtotal_float.replace(",", "") # remove any commas
        subtotal_float = float(subtotal_float)
        return subtotal_float

    def get_items_quantity_dict(self):
        """return a dictionary with key as prodcut_name and value as quantity"""
        cart_items = self.get_cart_items()
        quantities = {}
        for item in cart_items:
            product_name = item.find_element(By.CSS_SELECTOR, ".name.font-weight-medium").text
            quantity_item = item.find_element(By.NAME, "item.EnteredQuantity").get_attribute("value")
            quantity_item = int(quantity_item)
            quantities[product_name] = quantity_item
        return quantities

    def click_checkout(self):
        checkout_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn.btn-clear.btn-block.btn-action"))
        )
        return checkout_button.click()

    def cart_title(self):
        cart_message_title = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "no-item-title"))
        ).text
        return cart_message_title

    def clear_cart(self):
        """removes all the items from cart"""
        wait = WebDriverWait(self.driver, 3)
        while len(self.cart_items()) > 0:
            item_to_remove = self.bin_buttons()[0]
            item_to_remove.click()
            wait.until(EC.staleness_of(item_to_remove)) # Wait until the button has been removed


