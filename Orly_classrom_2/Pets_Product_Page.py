from selenium import webdriver
from selenium.webdriver.common.by import By


class PetsProductPage:
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver

    def table_data_rows(self):
        """ Returns all the table data rows in the products table, excluding the header """
        return self.driver.find_elements(By.CSS_SELECTOR,"table>tbody>tr")[1:]

    def product_id(self, row_index):
        """ Returns a product id in a specific row """
        return self.table_data_rows()[row_index].find_elements(By.TAG_NAME,"td")[0]

    def product_name(self, row_index):
        """ Returns a product name element in a specific row """
        return self.table_data_rows()[row_index].find_elements(By.TAG_NAME,"td")[1]

    def product_name_text(self, row_index):
        """ Returns a product name text in a specific row """
        return self.product_name(row_index).text

    def product_id_click(self, row_index):
        self.product_id(row_index).click()