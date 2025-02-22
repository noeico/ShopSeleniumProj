from unittest import TestCase
from selenium import webdriver
from qa12_selenium.Calc_Page import CalcPage
from time import sleep
from random import randint


class TestCalcPage(TestCase):
    def setUp(self):
        # Create a browser object (Open the browser)
        self.driver = webdriver.Chrome()
        # Go to the required URL
        self.driver.get("https://juliemr.github.io/protractor-demo/")
        # Maximize the window
        self.driver.maximize_window()
        # Define a timeout: In case an element is not found - wait 10 seconds
        self.driver.implicitly_wait(10)
        self.calc_page = CalcPage(self.driver)  # Create calc page object

    def test_calc_check_result(self):
        """ Calculate 5 * 9 and check the result """
        self.calc_page.type_number1("5")
        self.calc_page.choose_operator("*")
        self.calc_page.type_number2("9")
        self.calc_page.click_go()
        self.assertEqual("45", self.calc_page.final_result_text())

    def test_calc_check_empty_fields(self):
        """ Check that after a calculation is done, the numbers are empty. """
        self.calc_page.type_number1("10")
        self.calc_page.choose_operator("/")
        self.calc_page.type_number2("3")
        self.calc_page.click_go()
        self.calc_page.wait_for_result()
        self.assertEqual("",self.calc_page.number1_value())
        self.assertEqual("",self.calc_page.number2_value())

    def test_5_random_calculations(self):
        """ Perform 5 random calculations (with multiplication)
        and check the main result and the history top result for each calculation"""
        for i in range(5):
            num1 = randint(1,100)
            num2 = randint(1,100)
            self.calc_page.type_number1(str(num1))
            self.calc_page.type_number2(str(num2))
            self.calc_page.choose_operator("*")
            self.calc_page.click_go()
            result = num1*num2
            self.assertEqual(str(result), self.calc_page.final_result_text())
            self.assertEqual(str(result), self.calc_page.history_top_final_result_text())

    def tearDown(self):
        #self.driver.close()
        sleep(2)
        self.driver.quit()

