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

class LogInPage:
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver

    def user_name_field(self):
        user_name_input = self.driver.find_element(By.ID, "UsernameOrEmail")
        return user_name_input

    def password_field(self):
        password_input = self.driver.find_element(By.ID, "Password")
        return password_input

    def click_submit(self):
        submit_button = self.driver.find_element(By.CSS_SELECTOR, ".btn-primary.btn-lg")
        return submit_button.click()

