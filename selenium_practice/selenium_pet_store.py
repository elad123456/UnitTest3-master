from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import locale

service1 = Service(r"C:\Users\Admin\Documents\ELAD\chromedriver.exe")
driver = webdriver.Chrome(service=service1)
driver.get("https://petstore.octoperf.com/actions/Catalog.action")
driver.minimize_window()
driver.implicitly_wait(10)
wait=WebDriverWait(driver,10)
for i in range(5):
    animals = driver.find_elements(By.CSS_SELECTOR, "#SidebarContent>a>img")
    animal=random.choice(animals)
    animal.click()
    sleep(1)
    # wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"table>tbody>tr>td>a")))
    kinds=driver.find_elements(By.CSS_SELECTOR,"table>tbody>tr>td>a")
    kind=random.choice(kinds)
    kind.click()
    sleep(1)
    # wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"table>tbody>tr>td>a.Button")))
    versions=driver.find_elements(By.CSS_SELECTOR,"table>tbody>tr>td>a.Button")
    ver=random.choice(versions)
    ver.click()
    sleep(1)
    # wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"table>tbody>tr>td>input[type=submit]")))
    quantities=driver.find_elements(By.CSS_SELECTOR,"table>tbody>tr>td>input[type=text]")
    quantities[len(quantities) - 1].clear()
    sleep(1)
    quantities[len(quantities)-1].send_keys(str(random.randint(1,10)))
    sleep(1)
    quantities[len(quantities) - 1].send_keys(Keys.ENTER)
    sleep(1)
    if i!=4:
        for i in range(4):
            driver.back()

table=driver.find_element(By.CSS_SELECTOR,"table")
rows=table.find_elements(By.TAG_NAME,"tr")
sum=0
for row in rows[1:len(rows)-1]:
    quantity=int(row.find_element(By.CSS_SELECTOR,"td>input[type=text]").get_attribute("value"))
    values = row.find_elements(By.TAG_NAME, "td")
    price_pet=values[5].text
    price_pet=locale.atof(price_pet.strip("$"))
    sum+=quantity*price_pet
    print(sum)
results1=rows[-1].find_elements(By.TAG_NAME,"td")
result=results1[0].text
ezer=''
for i in range(len(result)):
    if result[i].isnumeric() or result[i]=='.':
        ezer+=result[i]
ezer=float(ezer)
print(ezer)
if ezer==sum:
    print("pass!!!!!!!!!!!!!!!!!!!!!!!!!!")
sleep(8)
# driver.close()


