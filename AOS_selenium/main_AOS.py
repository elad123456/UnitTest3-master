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
from home_page import *

service1 = Service(r"C:\Users\Admin\Documents\ELAD\chromedriver.exe")
driver = webdriver.Chrome(service=service1)
driver.get("https://advantageonlineshopping.com/#/")
driver.minimize_window()
driver.implicitly_wait(10)
wait=WebDriverWait(driver,10)
home=home_page(driver)
# home.category()[4].click()
home.user_emoji_click()
home.enter_username()
home.enter_password()
home.signin_click()
sleep(8)
# driver.close()
