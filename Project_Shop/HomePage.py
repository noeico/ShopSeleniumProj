from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def categories_list(self):
        """Returns a list with all the categories on the home page"""
        for i in range(2):  # try for two times
            try:
                return WebDriverWait(self.driver, 10).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".artlist-homepage-categories a span"))
                )
            except Exception:
                print("try again to reload")
                sleep(1)
        raise Exception("cant find category list")

    def click_on_category(self, category_name):
        """Click on a category by given category name"""
        categories = self.categories_list()

        for category in categories:
            if category.text == category_name:
                # wait until category is clickable
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(category)
                )
                category.click()
                return

    def get_title(self):
        return self.driver.find_element(By.CSS_SELECTOR,"#ph-title-6 h1").text

    def click_outside_cart_sidebar(self):
        """click outside the sidebar and wait until it closed"""
        body_element = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        body_element.click()

        # Wait until the sidebar is closed
        self.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".cart-sidebar")))

    def return_to_home_page(self):
        """Return to the home page by ensuring the home logo is clickable and clicking on it."""
        # Validate home logo appears and click on it
        home_logo = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".shopbar-col.shop-logo"))
        )
        home_logo.click()

        # Wait for the home page to reload
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".shopbar-col.shop-logo"))
        )






