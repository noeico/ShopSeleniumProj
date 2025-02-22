from selenium import webdriver
from selenium.webdriver.common.by import By


class PetsHomePage:
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver

    def categories_list(self):
        """ Returns the list of all the categories """
        return self.driver.find_elements(By.CSS_SELECTOR,"#SidebarContent>a")

    def category(self, category_index):
        """ Returns a specific category according to index """
        return self.categories_list()[category_index]

    