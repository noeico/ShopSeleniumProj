from itertools import product
from unittest import TestCase
from openpyxl.styles.builtins import title
from selenium import webdriver
from time import sleep
from random import randint, choice
import logging
import sys
from Project_Shop.CartSidebar import CartSidebar
from Project_Shop.HomePage import HomePage
from Project_Shop.CategoryPage import CategoryPage
from Project_Shop.ProductPage import ProductPage
from Project_Shop.Headers import Headers
from Project_Shop.ShoppingCartPage import ShoppingCartPage
from random import randint
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Project_Shop.LogInPage import LogInPage
from Project_Shop.CheckoutPages import CheckoutPages



class TestShop(TestCase):
    def setUp(self):
        # Create a browser object (Open the browser)
        self.driver = webdriver.Chrome()
        # Go to the required URL
        self.driver.get("https://bearstore-testsite.smartbear.com/")
        # Maximize the window
        self.driver.maximize_window()
        # Define a timeout: In case an element is not found - wait 10 seconds
        self.driver.implicitly_wait(10)
        self.home_page = HomePage(self.driver)
        self.category_page = CategoryPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.cart_sidebar = CartSidebar(self.driver)
        self.headers = Headers(self.driver)
        self.shopping_cart_page = ShoppingCartPage(self.driver)
        self.login_page = LogInPage(self.driver)
        self.checkout_pages = CheckoutPages(self.driver)
        #sleep(2)
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.handler = logging.StreamHandler(sys.stdout)
        self.handler.setLevel(logging.DEBUG)
        self.logger.addHandler(self.handler)
        # self.headers.click_on_shopping_basket()
        # self.cart_sidebar.clear_cart()
        # self.cart_sidebar.click_outside_cart_sidebar()


    def test_1(self):
        """Validate that transition pages, category pages, and product pages are correct."""
        chosen_category = "Soccer"
        # Validate category title is matched with the chosen category
        self.home_page.click_on_category(chosen_category)
        title_of_category = self.category_page.get_category_title()
        self.assertEqual(chosen_category , title_of_category)

        # Validate product title is matched with the chosen product
        chosen_product = self.category_page.random_product()
        chosen_product_text = chosen_product.text
        chosen_product.click()
        self.assertEqual(self.product_page.product_title().text , chosen_product_text)

        self.driver.back()
        # Validate the page returned back to category
        self.assertEqual(chosen_category , title_of_category)

        self.driver.back()
        # Validate the page returned to home page
        self.assertIn("Welcome" , self.home_page.get_title())


    def test_2(self):
        """Validate total quantity on cart sidebar is correct"""
        chosen_category = "Jackets"  # choose a category by name
        self.home_page.click_on_category(chosen_category)
        product1 = self.category_page.random_product()
        product2 = self.category_page.random_product()

        product1.click()
        self.product_page.update_selector_quantity("3")
        self.product_page.update_sum_of_quantities()
        self.product_page.click_add_to_cart()
        self.driver.back()

        product2.click()
        self.product_page.update_selector_quantity("2")
        self.product_page.update_sum_of_quantities() # update the sum of quantites
        self.product_page.click_add_to_cart()
        sum_of_quantities_from_pages = self.product_page.get_sum_of_quantities()
        sum_of_quantities_from_cart = self.product_page.calculate_quantities_from_cart()
        # Compare total here with total in cart
        self.assertEqual(sum_of_quantities_from_pages,sum_of_quantities_from_cart)

    def test_3(self):
        """Adding 3 different category products and validating that name,
        quantity, and price are correct on the cart sidebar."""

        chosen_category = "Watches"
        self.home_page.click_on_category(chosen_category)
        quantity = 2
        for each_product in range(3):
            # self.driver.back()
            self.category_page.click_on_random_product()
            self.product_page.add_title_to_titles_list()
            self.product_page.insert_price_to_dict()
            self.product_page.update_selector_quantity(str(quantity))
            self.product_page.insert_quantity_to_dict()
            self.product_page.click_add_to_cart()
            quantity += 1
            self.driver.back()

        self.headers.click_on_shopping_basket()
        prices_from_pages = self.product_page.get_price_dict()
        quantities_from_pages = self.product_page.get_quantity_dict()
        prices_from_cart = self.cart_sidebar.get_items_price_dict()
        quantities_from_cart = self.cart_sidebar.get_items_quantity_dict()

        self.logger.info(f"Products list is :")
        self.logger.info(self.product_page.get_products_titles_list())
        self.logger.info("")
        self.logger.info(f"Quantity from product pages for each product are :")
        self.logger.info(quantities_from_pages)
        self.logger.info("")
        self.logger.info(f"Unit price from product pages for each product are :")
        self.logger.info(prices_from_pages)
        self.logger.info("")

        self.logger.info(f"quantity for each product on cart side bar are: ")
        self.logger.info(quantities_from_cart)
        self.logger.info("")
        self.logger.info("prices for each product on cart sidebar are :")
        self.logger.info(prices_from_cart)

        sleep(2)
        self.assertEqual(prices_from_pages , prices_from_cart)
        self.assertEqual(quantities_from_pages , quantities_from_cart )
        sleep(2)

    def test_4(self):
        """Validate cart sidebar is update correctly after deleting one product from it"""

        chosen_category = "Golf"
        self.home_page.click_on_category(chosen_category)

        # Product 1
        self.category_page.click_on_random_product()
        self.product_page.click_add_to_cart()
        self.driver.back()

        # Product 2
        self.category_page.click_on_random_product()
        self.product_page.click_add_to_cart()

        # Save products name before delete
        product_names = [product.text for product in self.cart_sidebar.cart_products_names()]
        name_of_product1 = product_names[0]

        # delete the first product
        self.cart_sidebar.bin_buttons()[0].click()
        product_names.remove(name_of_product1)

        # wait for the product to remove from cart
        WebDriverWait(self.driver, 10).until(
            lambda driver: name_of_product1 not in [product.text for product in self.cart_sidebar.cart_products_names()]
        )

        # Validate the product was removed
        self.assertNotIn(name_of_product1, product_names)

        # Validate rest of the products are still in cart
        for each_product in product_names:
            self.assertIn(each_product, product_names)



    def test_5(self):
        """Checking automatic transition to the cart sidebar and shopping cart page."""

        chosen_category = "Sunglasses"
        self.home_page.click_on_category(chosen_category)
        self.category_page.click_on_random_product()

        self.product_page.click_add_to_cart()
        # Validate sidebar opened automatically
        self.assertTrue(self.cart_sidebar.is_cart_sidebar_open())

        # Validate sidebar disappear
        self.cart_sidebar.click_outside_cart_sidebar()
        self.assertTrue(self.cart_sidebar.is_cart_sidebar_closed)
        sleep(2)

        # Validate sidebar opened after clicking "Shopping Basket"
        self.headers.shopping_basket_button().click()
        self.assertTrue(self.cart_sidebar.is_cart_sidebar_open())

        # Validate "go to cart" button opens the "shopping cart" page
        self.cart_sidebar.click_go_to_cart()
        self.shopping_cart_page.get_title()
        self.assertEqual("Shopping cart", self.shopping_cart_page.get_title())

    def test_6(self):
        """Adding three different products with different quantities and validating
        that the subtotal in the cart and shopping page is correct."""

        products = [
            {"category": "Soccer", "name": "Street Football", "quantity": 2},
            {"category": "Basketball", "name": "High School Game Basketball", "quantity": 4},
            {"category": "Sunglasses", "name": "Ray-Ban Top Bar RB 3183", "quantity": 5}
        ]

        total_price = 0
        for product in products:
            self.home_page.return_to_home_page() # for the next rounds
            category_name = product["category"]
            product_name = product["name"]
            product_quantity = product["quantity"]

            self.home_page.click_on_category(category_name)
            self.category_page.click_on_product_by_name(product_name)
            self.product_page.update_selector_quantity(product_quantity)

            # Save quantity and price in a dictionary
            self.product_page.update_price_dict()
            self.product_page.insert_quantity_to_dict()

            # Calaculate final price for each product
            product_price_multiply_quantity = self.product_page.get_unit_price() * product_quantity
            total_price += product_price_multiply_quantity

            self.logger.info(
                f"the price from product page of {product_name} with {product_quantity} quantity is: {product_price_multiply_quantity}")
            self.logger.info("")
            self.product_page.click_add_to_cart()

        # Varify quantity from product pages match with cart quantity
        quantity_dict_from_pages = self.product_page.get_quantity_dict()
        quantity_dict_from_cart = self.cart_sidebar.get_items_quantity_dict()
        self.assertEqual(quantity_dict_from_pages, quantity_dict_from_cart)

        # Varify prices from product pages matche with cart prices
        prices_from_pages_dict = self.product_page.get_price_dict()
        prices_from_cart_dict = self.cart_sidebar.get_items_price_dict()
        self.logger.info(f"prices from cart are {prices_from_cart_dict}")
        self.logger.info(f"quantities from cart are : {quantity_dict_from_cart}")
        self.assertEqual(prices_from_pages_dict,prices_from_cart_dict)


        # verify subtotal price from cart is correct
        self.assertEqual(total_price, self.cart_sidebar.get_total_price_float())

        # validate subtotal price is correct for each product
        self.cart_sidebar.click_go_to_cart()
        sleep(3)
        len_of_lists = len(self.shopping_cart_page.list_of_units_price())
        for x in range(len_of_lists):
            unit_price = self.shopping_cart_page.list_of_units_price()[x]
            quantity_units = self.shopping_cart_page.list_quantity_per_product()[x]
            subtotal_unit = self.shopping_cart_page.list_unit_subtotal()[x]
            self.assertEqual(unit_price * quantity_units, subtotal_unit)


    def test_7(self):
        """Validate change quantities on shopping page affects correctly on the subtotal prices"""

        category_name_1 = "Watches"
        product_name_1 = "TRANSOCEAN CHRONOGRAPH"
        product_quantity_1 = 2

        category_name_2 = "Shoes"
        product_name_2 = "COOGEE LOW M"
        product_quantity_2 = 4

        self.home_page.click_on_category(category_name_1)
        self.category_page.click_on_product_by_name(product_name_1)
        self.product_page.update_selector_quantity(str(product_quantity_1))
        self.product_page.click_add_to_cart()
        self.home_page.return_to_home_page()

        self.home_page.click_on_category(category_name_2)
        self.category_page.click_on_product_by_name(product_name_2)
        self.product_page.update_selector_quantity(str(product_quantity_2))
        self.product_page.click_add_to_cart()
        self.cart_sidebar.click_go_to_cart()

        # Changing quantity for first product
        self.shopping_cart_page.set_quantity(0,"10")
        # Changing quantity for second product
        self.shopping_cart_page.set_quantity(1, "20")
        sleep(2)

        # Check that the quantity of products actually changes
        self.assertEqual(self.shopping_cart_page.list_quantity_per_product()[0], 10)
        self.assertEqual(self.shopping_cart_page.list_quantity_per_product()[1], 20)

        # Validate that the subtotal for product 1 changed correctly
        unit_price_prod_1 = self.shopping_cart_page.list_of_units_price()[0]
        updated_quantity_prod_1 = self.shopping_cart_page.list_quantity_per_product()[0]
        subtotal_of_product = self.shopping_cart_page.list_unit_subtotal()[0]
        self.assertEqual(unit_price_prod_1 * updated_quantity_prod_1 , subtotal_of_product)

        # Validate that the subtotal for product 2 changed correctly
        unit_price_prod_2 = self.shopping_cart_page.list_of_units_price()[1]
        updated_quantity_prod_2 = self.shopping_cart_page.list_quantity_per_product()[1]
        subtotal_of_product = self.shopping_cart_page.list_unit_subtotal()[1]
        self.assertEqual(unit_price_prod_2 * updated_quantity_prod_2, subtotal_of_product)

        # Validate that the subtotal of all products changed correctly
        calc_subtotal = self.shopping_cart_page.calc_subtotal()
        subtotal_as_shown = self.shopping_cart_page.get_subtotal()
        self.assertEqual(calc_subtotal , subtotal_as_shown)
        self.home_page.return_to_home_page()
        self.headers.click_on_shopping_basket()
        subtotal_cart_sidebar = self.cart_sidebar.get_total_price_float()

        # Validate subtotal of cart sidebar is correct
        self.assertEqual(calc_subtotal , subtotal_cart_sidebar)



    def test_8(self):
        """Validates the checkout process, order confirmation, and cart status."""

        category_name_1 = "Watches"
        product_name_1 = "TRANSOCEAN CHRONOGRAPH"

        category_name_2 = "Shoes"
        product_name_2 = "COOGEE LOW M"

        user_name = "Noei"
        password = "noei12"

        # Product 1
        self.home_page.click_on_category(category_name_1)
        self.category_page.click_on_product_by_name(product_name_1)
        self.product_page.click_add_to_cart()
        self.home_page.return_to_home_page()

        # Product 2
        self.home_page.click_on_category(category_name_2)
        self.category_page.click_on_product_by_name(product_name_2)
        self.product_page.click_add_to_cart()
        self.cart_sidebar.click_checkout()

        self.login_page.user_name_field().send_keys("Noei")
        self.login_page.password_field().send_keys("noei12")
        self.login_page.click_submit()

        self.checkout_pages.click_checkout()
        self.checkout_pages.click_this_bill()
        self.checkout_pages.click_ship_to_this_address()
        self.checkout_pages.click_next_shiping_page()
        self.checkout_pages.click_next_payment_page()
        self.checkout_pages.check_checkbox()
        self.checkout_pages.click_confirm()

        # Validate order has confirmed and order detail number is matched
        order_number = self.checkout_pages.get_order_number()
        self.assertEqual(self.checkout_pages.order_title(),"Your order has been received")
        self.checkout_pages.click_order_details_button()
        self.assertEqual(order_number,self.checkout_pages.get_order_number_from_order_details_page())

        # Validate caer is empty

        self.headers.click_on_shopping_basket()
        self.assertEqual(self.cart_sidebar.cart_title(), "Shopping cart empty")


        sleep(3)

    def test_9(self):
        """Validate login and logout process"""

        self.headers.click_login()
        self.login_page.user_name_field().send_keys("Noei")
        self.login_page.password_field().send_keys("noei12")
        self.login_page.click_submit()
        self.assertEqual(self.headers.get_logged_in_username_text(), "Noei".upper())
        self.headers.click_on_user_name()
        self.headers.click_log_out()
        self.assertEqual(self.headers.log_in_button().text,"Log in".upper())

    def tearDown(self):
        if self.cart_sidebar.is_cart_sidebar_closed():
            self.home_page.return_to_home_page()
            self.headers.click_on_shopping_basket()
            self.cart_sidebar.clear_cart()
        elif self.cart_sidebar.is_cart_sidebar_open():
            self.cart_sidebar.clear_cart()
            self.cart_sidebar.click_outside_cart_sidebar()
            self.home_page.return_to_home_page()
        self.driver.quit()
