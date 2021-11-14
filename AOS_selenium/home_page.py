import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from random import *

class home_page:
    def __init__(self,driver:webdriver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)

    def category(self):
        categories_elements=self.driver.find_elements(By.CSS_SELECTOR,".rowSection>div")
        categories_elements.remove(categories_elements[2])
        return categories_elements

    def click_category(self):
        random.choice(self.category()).click()

    def user_emoji(self):
        return self.driver.find_element(By.ID,"menuUser")

    def user_emoji_click(self):
        self.user_emoji().click()
    def username(self):
        return self.driver.find_element(By.NAME,"username")
    def enter_username(self):
        self.username().clear()
        self.username().send_keys('elad1234')
    def password(self):
        return self.driver.find_element(By.NAME,"password")
    def enter_password(self):
        self.password().clear()
        self.password().send_keys('Thbyrby145')
    def sign_in(self):
        return self.driver.find_element(By.ID,"sign_in_btnundefined")
    def signin_click(self):
        self.wait.until(EC.element_to_be_clickable((By.ID,"sign_in_btnundefined")))
        self.wait.until(EC.text_to_be_present_in_element_attribute((self.password())))
        self.sign_in().click()



