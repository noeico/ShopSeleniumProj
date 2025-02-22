from unittest import TestCase
from selenium import webdriver
from qa12_selenium.Pets_Home_Page import PetsHomePage
from qa12_selenium.Pets_Product_Page import PetsProductPage
from qa12_selenium.Pets_Items_Page import PetsItemPage
from time import sleep
from random import randint, choice


class TestPetsPage(TestCase):
    def setUp(self):
        # Create a browser object (Open the browser)
        self.driver = webdriver.Chrome()
        # Go to the required URL
        self.driver.get("https://petstore.octoperf.com/actions/Catalog.action")
        # Maximize the window
        self.driver.maximize_window()
        # Define a timeout: In case an element is not found - wait 10 seconds
        self.driver.implicitly_wait(10)
        self.home_page = PetsHomePage(self.driver)
        self.product_page = PetsProductPage(self.driver)
        self.items_page = PetsItemPage(self.driver)

    def test_add_item_to_cart(self):
        choice(self.home_page.categories_list()).click()       # click random category
        product_rows = self.product_page.table_data_rows()
        random_index = randint(0, len(product_rows)-1)         # choose random index of product
        print(f"We chose {self.product_page.product_name_text(random_index)}")
        self.product_page.product_id_click(random_index)

        items_rows = self.items_page.table_rows()
        random_index = randint(0, len(items_rows) - 1)  # choose random index of item
        self.items_page.click_add_to_cart(random_index)

    def tearDown(self):
        sleep(2)
        self.driver.quit()