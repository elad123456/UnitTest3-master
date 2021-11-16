from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import locale
from home_page_class import home_page
from category_page_class import category_page
from product_page_class import product_page
from shopping_cart_page_class import shopping_cart_page

service1 = Service(r"C:\Users\Admin\Documents\ELAD\chromedriver.exe")
driver = webdriver.Chrome(service=service1)
driver.get("https://advantageonlineshopping.com/#/")
driver.maximize_window()
driver.implicitly_wait(10)
wait=WebDriverWait(driver,10)
home=home_page(driver)
category=category_page(driver)
product=product_page(driver)
shopping_cart_page=shopping_cart_page(driver)
# home.user_emoji_click()
# home.enter_username()
# home.enter_password()
# home.sign_in_click()
# home.user_emoji_click()
# home.click_sign_out()
# sleep(3)
# driver.close()
home.click_category(0)
category.click_product("25")
product.click_add_to_cart()
product.click_back_to_home()
home.click_category(1)
category.click_product("16")
product.click_add_to_cart()
driver.back()
# home.click_shopping_cart_window()
# # print(driver.find_element(By.CSS_SELECTOR,"[class='roboto-regular center sticky fixedImportant ng-binding']").text[:13])
# print(shopping_cart_page.price())
# home.click_shopping_cart_window()
# edits=shopping_cart_page.edit_buttons()
# for edit in edits:
#     shopping_cart_page.click_on_edit()
#     product.change_quantity()
#     product.click_add_to_cart()

sleep(20)
driver.close()