from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from pet_store_cart import *
from time import sleep

service1 = Service(r"C:\Users\Admin\Documents\ELAD\chromedriver.exe")
driver = webdriver.Chrome(service=service1)
driver.get("https://petstore.octoperf.com/actions/Cart.action?addItemToCart=&workingItemId=EST-1")
driver.minimize_window()
driver.implicitly_wait(10)
wait=WebDriverWait(driver,10)
cart_page=pet_store_cart(driver)
# cart_page.return_to_main_menu()
# print(cart_page.total_price_last_row())
# cart_page.update_quantity_of_pet(1,100)
# cart_page.click_specific_remove(1)
print(cart_page.sub_total())
sleep(3)
driver.close()