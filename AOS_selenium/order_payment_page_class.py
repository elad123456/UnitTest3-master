from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import random
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys



class order_payment_page:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,10)

    def username(self):
        username=self.driver.find_element(By.NAME,"usernameInOrderPayment")
        return username
    def enter_username(self,name):
        username=self.username()
        username.click()
        username.clear()
        username.send_keys(name)

    def password(self):
        password=self.driver.find_element(By.NAME,"passwordInOrderPayment")
        return password
    def enter_password(self,passw):
        password=self.password()
        password.click()
        password.clear()
        password.send_keys(passw)

    def click_login(self):
        login=self.driver.find_element(By.ID,"login_btnundefined")
        login.click()
    def click_next(self):
        next=self.driver.find_element(By.ID,"next_btn")
        next.click()
    def click_master_credit(self):
        master_credit = self.driver.find_element(By.NAME, "masterCredit")
        master_credit.click()
    def card_number(self):
        return self.driver.find_element(By.NAME,"card_number")
    def CVV_number(self):
        return self.driver.find_element(By.NAME,"cvv_number")
    def date_mounth(self):
        return Select(self.driver.find_element(By.NAME,"mmListbox"))
    def date_year(self):
        return Select(self.driver.find_element(By.NAME,"yyyyListbox"))
    def card_holder_name(self):
        return self.driver.find_element(By.NAME,"cardholder_name")
    def fill_master_card_details(self,card_number,cvv_number,holder_name,mm,yyyy):
        self.wait.until(EC.visibility_of_element_located((By.NAME,"card_number")))
        card_num_element=self.card_number()
        card_num_element.send_keys(Keys.DELETE)
        card_num_element.send_keys(card_number)
        CVV_element=self.CVV_number()
        CVV_element.click()
        CVV_element.clear()
        CVV_element.send_keys(cvv_number)
        holder_element=self.card_holder_name()
        holder_element.clear()
        holder_element.send_keys(holder_name)
        self.date_mounth().select_by_index(mm)
        self.date_year().select_by_index(yyyy)

    def click_pay_now(self):
         pay_now=self.driver.find_element(By.IDd,"pay_now_btn_MasterCredit")
         self.wait.until(EC.visibility_of_element_located((By.NAME,"pay_now_btn_MasterCredit")))
         pay_now.click()
    def click_edit(self):
         edit=self.driver.find_element(By.CLASS_NAME,"edit")
         edit.click()





