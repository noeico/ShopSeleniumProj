import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

appium_server_url_local = 'http://localhost:4723/wd/hub'
capabilities  = dict(
    platformName='Android',
    deviceName='Pixel7a',
    udid="emulator-5554",
    platformVersion="34",
    appPackage='com.google.android.calculator',
    newCommandTimeout= 120,
    appActivity='com.android.calculator2.Calculator',
    language='en',
    locale='US'
)


class firstTestAppium(unittest.TestCase):

    def setUp(self) -> None:

        self.driver = webdriver.Remote(appium_server_url_local, capabilities)
        self.driver.implicitly_wait(10)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_calculate_multiple_numbers(self)->None:
        digit_1 = self.driver.find_element(by=AppiumBy.ID, value='com.google.android.calculator:id/digit_1')
        digit_5 = self.driver.find_element(by=AppiumBy.ID, value='com.google.android.calculator:id/digit_5')
        multiple = self.driver.find_element(by=AppiumBy.ID,value = 'com.google.android.calculator:id/op_mul')
        result_nemu = self.driver.find_element(by=AppiumBy.ID,value='com.google.android.calculator:id/result_preview')

        digit_1.click()
        multiple.click()
        digit_5.click()
        results_text = result_nemu.text

        assert results_text =='5',"The result of multiple 1 by 5 is not 5 as expected "


