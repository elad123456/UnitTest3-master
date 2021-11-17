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

# defin the chrome service
service1 = Service(r"C:\Users\Admin\Documents\ELAD\chromedriver.exe")

# defin the
driver = webdriver.Chrome(service=service1)
driver.minimize_window()
# get into a site(google in this case)
driver.get("https://www.google.co.il/?hl=iw")

# give the programming 10 seconds to find the element
driver.implicitly_wait(10)

# using an element
google_search_line=driver.find_element(By.CSS_SELECTOR,"body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input")
# using thr element
google_search_line.send_keys("python")

# # using search bottom
#search_bottom= driver.find_element(By.CSS_SELECTOR,"body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.FPdoLc.lJ9FBc > center > input.gNO89b")
# # click on search bottom
# search_bottom.click()
google_search_line.send_keys(Keys.ENTER)




# the programing run 2 seconds
sleep(2)
if driver.find_element(By.CSS_SELECTOR,"input.gLFyf").get_attribute("value")=="python":
    print("pass")
else:
    print("fail")
# close the driver
driver.close()
