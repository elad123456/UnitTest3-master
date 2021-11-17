#שימוש בסלניום
from selenium import webdriver
# שימוש בסרוויס חרום או פייר פוקס
from selenium.webdriver.chrome.service import Service
# שימוש בקלאס טיים כדי להשהות את ההרצה
from time import sleep
# שימוש במקלדת
from selenium.webdriver.common.keys import Keys
# שימוש באלמנטים
from selenium.webdriver.common.by import By

service1 = Service(r"C:\Users\Admin\Documents\ELAD\chromedriver.exe")
driver = webdriver.Chrome(service=service1)
driver.minimize_window()

driver.get("https://www.rail.co.il/")
location=driver.find_element(By.CSS_SELECTOR,"#trainSearchMain > div > div > div > div.col-md-2.col-sm-5.col-xs-10.fromBox > div.typeahead.ng-isolate-scope > input")
where=driver.find_element(By.CSS_SELECTOR,"#trainSearchMain > div > div > div > div.col-md-2.col-sm-5.col-xs-10.toBox > div.typeahead.ng-isolate-scope > input")
location.send_keys("אשקלון")
location.send_keys(Keys.ENTER)
where.send_keys("בנימינה")
where.send_keys(Keys.ENTER)
search=driver.find_element(By.CSS_SELECTOR,"#trainSearchMain > div > div > div > div.col-md-2.col-sm-11.col-xs-10.searchBtnBox > button")
search.click()

sleep(2)
driver.close()