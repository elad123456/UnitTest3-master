from selenium import webdriver
from selenium.webdriver.common.by import By

class pet_store_cart:
    def __init__(self,driver:webdriver):
        self.driver=driver

    def return_to_main_menu(self):
        self.driver.find_element(By.CSS_SELECTOR,"#BackLink>a").click()

    def last_row(self):
        table = self.driver.find_element(By.CSS_SELECTOR, "table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        return rows[-2]
    def total_price_last_row(self):
        cells=self.last_row().find_elements(By.TAG_NAME,"td")
        return cells[-2].text
    def click_specific_remove(self,num_pet):
        table = self.driver.find_element(By.CSS_SELECTOR, "table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        cells = rows[num_pet].find_elements(By.TAG_NAME, "td")
        cells[-1].find_element(By.TAG_NAME,"a").click()
    def update_quantity_of_pet(self,num_of_pet,quantity):
        table = self.driver.find_element(By.CSS_SELECTOR, "table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        cells = rows[num_of_pet].find_elements(By.TAG_NAME, "td")
        qu=cells[4].find_element(By.TAG_NAME, "input")
        qu.clear()
        qu.send_keys(quantity)
    def sub_total(self):
        table = self.driver.find_element(By.CSS_SELECTOR, "table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        cells = rows[-1].find_elements(By.TAG_NAME, "td")
        text= cells[0].text
        ezer=''
        for value in text:
            try:
                if 0<=int(value)<=9:
                    ezer+=value
            except:
                pass
            if value=='.':
                ezer+=value
        return float(ezer)



