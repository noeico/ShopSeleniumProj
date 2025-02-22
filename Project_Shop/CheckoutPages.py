from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPages:
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver

    def click_checkout(self):
        checkout_button = self.driver.find_element(By.NAME, "checkout")
        return checkout_button.click()

    def first_name_field(self):
        first_name_input = self.driver.find_element(By.NAME,"NewAddress.FirstName")
        return first_name_input

    def last_name_field(self):
        last_name_input = self.driver.find_element(By.NAME, "NewAddress.LastName")
        return last_name_input

    def click_this_bill(self):
        address_button = self.driver.find_element(By.CSS_SELECTOR,".select-billing-address-button")
        return address_button.click()

    def click_next_shiping_page(self):
        next_step_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".shipping-method-next-step-button"))
        )
        return next_step_button.click()

    def click_next_payment_page(self):
        next_step_button = self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-warning.btn-lg.payment-method-next-step-button")
        return next_step_button.click()

    def check_checkbox(self):
        checkbox = self.driver.find_element(By.ID,"termsofservice")
        checkbox.click()

    def click_confirm(self):
        confirm_button = self.driver.find_element(By.CSS_SELECTOR,".btn-buy span")
        return confirm_button.click()

    def click_this_address(self):
        button_address = self.driver.find_element(By.CSS_SELECTOR,".address-button")
        button_address.click()

    def click_ship_to_this_address(self):
        button = self.driver.find_element(By.XPATH, "//button[contains(@class, 'select-shipping-address-button')]")
        button.click()

    def get_order_number(self):
        order_number = self.driver.find_element(By.XPATH,"//div[@class='body fs-h5']/p/a/strong")
        return order_number.text

    def order_title(self):
        purchased_title = self.driver.find_element(By.CSS_SELECTOR,"h1.heading-title.font-weight-light")
        return purchased_title.text

    def click_order_details_button(self):
        order_details_button = self.driver.find_element(By.CSS_SELECTOR,"a.btn.btn-warning span")
        return order_details_button.click()

    def get_order_number_from_order_details_page(self):
        order_number = self.driver.find_element(By.CSS_SELECTOR,"h1.h2.mb-0 small")
        return order_number.text