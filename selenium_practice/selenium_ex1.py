from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

service1 = Service(r"C:\Users\Admin\Documents\ELAD\chromedriver.exe")
driver = webdriver.Chrome(service=service1)
driver.get("https://phptravels.net/api/admin")
driver.minimize_window()
driver.implicitly_wait(10)
email=driver.find_element(By.CSS_SELECTOR,"input[type='text'][name='email']")
email.send_keys("admin@phptravels.com")
password=driver.find_element(By.CSS_SELECTOR,"input[type='password'][name='password']")
password.send_keys("demoadmin")
password.send_keys(Keys.ENTER)
driver.find_element(By.LINK_TEXT,"Cars").click()
driver.find_element(By.LINK_TEXT,"Locations").click()
sleep(7)
driver.close()