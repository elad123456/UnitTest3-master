from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import random
from time import sleep
from product_page_class import product_page

class shopping_cart_page:
    def __init__(self,driver):
        self.driver=driver
        self.product_page=product_page(self.driver)
        self.wait=WebDriverWait(self.driver,10)
    def title(self):
        title=self.driver.find_element(By.CSS_SELECTOR,"[class='roboto-regular center sticky fixedImportant ng-binding']")
        return title
    def title_text_shopping_cart(self):
        text=self.title().text
        return text[:13]
    def text_price(self):
        total_price_elements=self.driver.find_elements(By.CLASS_NAME,"cart-total")
        return total_price_elements[0].text
    def price(self):
        price=''
        for w in self.text_price():
            if w.isnumeric() or w=='.':
                price+=w
        return price
    def edit_buttons(self):
        edits=self.driver.find_elements(By.CSS_SELECTOR,"[class='edit ng-scope']")
        return edits
    def click_on_edit(self,edit):
        # self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[class='edit ng-scope']")))
        edit.click()

