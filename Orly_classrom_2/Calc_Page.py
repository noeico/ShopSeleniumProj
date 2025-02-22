from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class CalcPage:
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver

    def number1(self):
        """Returns the first number element"""
        return self.driver.find_element(By.CSS_SELECTOR,"[ng-model='first']")

    def number2(self):
        """Returns the second number element"""
        return self.driver.find_element(By.CSS_SELECTOR,"[ng-model='second']")

    def operator(self):
        """Returns the operator element"""
        return self.driver.find_element(By.CSS_SELECTOR,"[ng-model='operator']")

    def go(self):
        """Return the go button element"""
        return self.driver.find_element(By.ID,"gobutton")

    def result(self):
        """Return the result element"""
        return self.driver.find_element(By.CSS_SELECTOR,"h2[class='ng-binding']")

    def type_number1(self, num_value: str):
        """Type 'num' in number1 element"""
        self.number1().send_keys(num_value)

    def type_number2(self, num_value: str):
        """Type 'num' in number2 element"""
        self.number2().send_keys(num_value)

    def choose_operator(self, op_value: str):
        """Choose operator in drop down element"""
        operator_dropdown = Select(self.operator())
        operator_dropdown.select_by_visible_text(op_value)

    def click_go(self):
        self.go().click()

    def result_text(self):
        """Return the result text"""
        return self.result().text

    def wait_for_result(self):
        """ Wait until the result is ready """
        while self.result_text()[0] == ".":
            pass

    def final_result_text(self):
        """Return the result text after the calculation is done"""
        self.wait_for_result()
        return self.result_text()

    def number1_value(self):
        """Return the first number value"""
        return self.number1().get_attribute("value")

    def number2_value(self):
        """Return the second number value"""
        return self.number2().get_attribute("value")

    def operator_value(self):
        """Return the operator value"""
        return self.operator().get_attribute("value")

    def history_top_result(self):
        """Return the last result element from the history table"""
        return self.driver.find_element(By.XPATH,"//tbody/tr[1]/td[3]")

    def history_top_final_result_text(self):
        """Return the last result text from the history table"""
        self.wait_for_result()
        return self.history_top_result().text