from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from unittest import TestCase
service1 = Service(r"C:\Users\Admin\Documents\ELAD\chromedriver.exe")
driver = webdriver.Chrome(service=service1)
driver.get("https://opensea.io/")
driver.maximize_window()
driver.implicitly_wait(10)
wait=WebDriverWait(driver,10)