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
driver.get("https://juliemr.github.io/protractor-demo/")
driver.minimize_window()
driver.implicitly_wait(10)
driver.find_element(By.CSS_SELECTOR,"[ng-model='first']").send_keys(5)
driver.find_element(By.CSS_SELECTOR,"[ng-model='second']").send_keys(6)
Select(driver.find_element(By.CSS_SELECTOR,"[ng-model='operator']")).select_by_index(3)
driver.find_element(By.ID,"gobutton").click()
wait= WebDriverWait(driver,10)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"tr.ng-scope")))
result=driver.find_element(By.CSS_SELECTOR,"h2.ng-binding")
if result.text=="30":
    print("pass")
else:
    print("fail")
driver.close()
