from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from unittest import TestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


service1 = Service(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
driver = webdriver.Chrome(service=service1)
driver.get("https://opensea.io/")
driver.maximize_window()
driver.implicitly_wait(10)
wait=WebDriverWait(driver,10)

google=driver.find_element(By.CSS_SELECTOR,"#input")
sleep(2)
driver.close()