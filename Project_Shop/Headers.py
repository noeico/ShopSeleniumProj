from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Headers:
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver

    def shopping_basket_button(self):
        """Wait for the shopping basket button to be visible and return it."""
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, "shopbar-cart"))
        )

    def click_on_shopping_basket(self):
        return self.shopping_basket_button().click()

    def log_in_button(self):
        login_button = self.driver.find_element(By.XPATH, "//a[@class='menubar-link']/span[text()='Log in']")
        return login_button

    def click_login(self):
        self.log_in_button().click()

    def get_logged_in_user_name_element(self):
        user_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a.menubar-link span[title]'))  # מחפש ספציפית את ה-title
        )
        return user_element

    def get_logged_in_username_text(self):
        return self.get_logged_in_user_name_element().text

    def click_on_user_name(self):
        return self.get_logged_in_user_name_element().click()

    def click_log_out(self):
        log_out_button = self.driver.find_element(By.LINK_TEXT, "Log out")
        return log_out_button.click()
