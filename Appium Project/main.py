import unittest
from appium import webdriver as mobile
from appium.webdriver.common.appiumby import AppiumBy
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver as web



appium_server_url_local = 'http://localhost:4723/wd/hub'

capabilities = dict(
    platformName='Android',
    deviceName='Pixel7a',
    udid="emulator-5554",
    platformVersion="34",
    appActivity='com.android.calculator2.Calculator',
    appPackage='com.google.android.calculator',
    newCommandTimeout=120,
    language='en',
    locale='US'
)


class seleniumAndAppiumTest(unittest.TestCase):
    print("Start test")

    def setUp(self) -> None:
        self.driver_mobile = mobile.Remote(appium_server_url_local, capabilities)
        self.driver_mobile.implicitly_wait(10)

        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver_web = web.Chrome(service=service)
        self.driver_web = driver_web

    def tearDown(self) -> None:
        if self.driver_mobile:
            self.driver_mobile.quit()

    def test1(self):
        print("into test1")
        self.driver_web.get("http://www.google.com")
        digit_one = self.driver_mobile.find_element(by=AppiumBy.ID, value='com.google.android.calculator:id/digit_1')
        digit_one.click()
        a = 1