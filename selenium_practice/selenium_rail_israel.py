from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

service1 = Service(r"C:\Users\Admin\Documents\ELAD\chromedriver.exe")
driver = webdriver.Chrome(service=service1)
driver.get("https://www.rail.co.il/")
driver.minimize_window()
driver.implicitly_wait(10)

location=driver.find_element(By.CSS_SELECTOR,"#trainSearchMain > div > div > div > div.col-md-2.col-sm-5.col-xs-10.fromBox > div.typeahead.ng-isolate-scope > input")
location.send_keys("אשקלון")
location.send_keys(Keys.ENTER)
where=driver.find_element(By.CSS_SELECTOR,"#trainSearchMain > div > div > div > div.col-md-2.col-sm-5.col-xs-10.toBox > div.typeahead.ng-isolate-scope > input")
where.send_keys("אחיהוד")
where.send_keys(Keys.ENTER)
search=driver.find_element(By.CSS_SELECTOR,"button.ng-binding[ng-click='getAllData()']")
search.click()
wait= WebDriverWait(driver,10)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"span[class='station_name ng-binding']")))
if driver.find_element(By.CSS_SELECTOR,"span[class='station_name ng-binding']").text=="אשקלון":
    print("pass")
else:
    print("fail")
sleep(5)
driver.close()