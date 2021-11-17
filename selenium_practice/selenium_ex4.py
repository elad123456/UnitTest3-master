from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service1 = Service(r"C:\Users\Admin\Documents\ELAD\chromedriver.exe")
driver = webdriver.Chrome(service=service1)
driver.get("http://demo.guru99.com/test/newtours/")
driver.minimize_window()
driver.implicitly_wait(10)
username=driver.find_element(By.CSS_SELECTOR,"[name='userName']")
username.send_keys("tutorial")
sleep(1)
password=driver.find_element(By.CSS_SELECTOR,"[name='password']")
password.send_keys("tutorial")
sleep(1)
password.send_keys(Keys.ENTER)
sleep(1)
driver.find_element(By.LINK_TEXT,"Flights").click()
sleep(1)
driver.find_element(By.CSS_SELECTOR,"[value='oneway']").click()
sleep(1)
driver.find_element(By.CSS_SELECTOR,"[value='First']").click()
sleep(1)
select_airline=Select(driver.find_element(By.CSS_SELECTOR,"[name='airline']"))
select_airline.select_by_index(1)
sleep(1)
driver.find_element(By.CSS_SELECTOR,"[name='findFlights']").click()
sleep(1)
driver.close()