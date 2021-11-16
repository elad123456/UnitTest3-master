from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import locale
from home_page_class import home_page
from category_page_class import category_page
from product_page_class import product_page
from unittest import TestCase
from shopping_cart_page_class import shopping_cart_page
from order_payment_page_class import order_payment_page

class tests_AOS(TestCase):
    def setUp(self):
        print("setUp")
        service1 = Service(r"C:\Users\Admin\Documents\ELAD\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service1)
        self.driver.get("https://advantageonlineshopping.com/#/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.home=home_page(self.driver)
        self.category=category_page(self.driver)
        self.product=product_page(self.driver)
        self.shopping_cart_page=shopping_cart_page(self.driver)
        self.order_payment=order_payment_page(self.driver)
    def tearDown(self):
        sleep(10)
        self.driver.close()
        print("tearDown")

    def test1(self):
        total_items = 0
        for i in range(3):
            self.home.click_category(i)
            if i==0:
                self.category.click_product("25")
            elif i==1:
                self.category.click_product("16")
            elif i==2:
                self.category.click_product("9")
            quantity = self.product.change_quantity()
            total_items += quantity
            self.product.click_add_to_cart()
            self.product.click_back_to_home()

        number_of_items=self.home.rerturn_the_num_of_items()
        self.assertEqual(total_items,int(number_of_items))

    def test2(self):
        qu=[]
        co=[]
        names=[]
        price=[]
        for i in range(3):
            self.home.click_category(i+1)
            if i == 0:
                self.category.click_product("16")
            elif i == 1:
                self.category.click_product("9")
            elif i == 2:
                self.category.click_product("28")
            quantity=self.product.change_quantity()
            qu.append(quantity)
            # sleep(1)
            # if i==2:
            #     sleep(20)
            color=self.product.choose_color()
            co.append(color)

            product_name=self.product.product_name()
            names.append(product_name)
            pr=self.product.price()
            price.append(float(pr))
            self.product.click_add_to_cart()
            self.product.click_back_to_home()
        names.reverse()
        self.assertListEqual(names,self.home.names_in_cart())
        qu.reverse()
        self.assertListEqual(qu,self.home.quantities_in_cart())
        co.reverse()
        price.reverse()
        print(co)
        print(self.home.colors_in_cart())
        self.assertListEqual(self.home.colors_in_cart(),co)
        except_price = 0.0
        for i in range(3):
            except_price += qu[i] * price[i]
        # self.assertListEqual(self.home.colors_in_cart(),co)
        self.assertEqual(round(except_price,2),self.home.price())

    def test3(self):
        total_items = 0
        for i in range(3):
            self.home.click_category(i+1)
            if i == 0:
                self.category.click_product("16")
            elif i == 1:
                self.category.click_product("9")
            elif i == 2:
                self.category.click_product("28")
            self.product.click_add_to_cart()
            self.product.click_back_to_home()

        number_of_products=self.home.len_of_products_in_Cart()
        self.home.click_remove()
        number_products_after_remove=self.home.len_of_products_in_Cart()
        self.assertEqual(number_of_products,number_products_after_remove+1)
    def test4(self):
        self.home.click_category(0)
        self.category.click_product("25")
        self.product.click_add_to_cart()
        self.product.click_back_to_home()
        self.home.click_shopping_cart_window()
        text=self.shopping_cart_page.title_text_shopping_cart()
        self.assertEqual(text,'SHOPPING CART')
    def test5(self):
        qu = []
        names = []
        price = []
        for i in range(3):
            self.home.click_category(i + 1)
            if i == 0:
                self.category.click_product("16")
            elif i == 1:
                self.category.click_product("9")
            elif i == 2:
                self.category.click_product("28")
            quantity = self.product.change_quantity()
            qu.append(quantity)
            product_name = self.product.product_name()
            names.append(product_name)
            pr = self.product.price()
            price.append(float(pr))
            print(f"name: {product_name}, quantity: {quantity}, price: {float(pr)}")
            self.product.click_add_to_cart()
            self.product.click_back_to_home()
        self.home.click_shopping_cart_window()
        total_price=self.shopping_cart_page.price()
        exept_price=0.0
        for i in range(3):
            exept_price += qu[i] * price[i]
        print(exept_price,total_price)
        total_price=float(total_price)
        total_price=round(total_price,2)
        self.assertEqual(round(exept_price,2),total_price)

    def test6(self):
        qu = []
        for i in range(2):
            self.home.click_category(i)
            if i == 0:
                self.category.click_product("25")
            elif i == 1:
                self.category.click_product("16")
            quantity = self.product.change_quantity()
            qu.append(quantity)
            self.product.click_add_to_cart()
            self.product.click_back_to_home()
        self.home.click_shopping_cart_window()
        edits=self.shopping_cart_page.edit_buttons()
        for i in edits:
            sleep(7)
            i.click()
            self.product.change_quantity()
            self.product.click_add_to_cart()
    def test7(self):
        self.home.click_category(1)
        self.category.click_product("16")
        self.driver.back()
        self.assertEqual(self.category.category_title(),"TABLETS")
        self.driver.back()
        self.assertEqual(self.home.text_in_home(), "SPECIAL OFFER")
    def test8(self):
        for i in range(3):
            self.home.click_category(i)
            if i == 0:
                self.category.click_product("25")
            elif i == 1:
                self.category.click_product("16")
            elif i == 2:
                self.category.click_product("9")
            self.product.click_add_to_cart()
            self.product.click_back_to_home()
        self.home.click_shopping_cart_window()
        self.home.click_checkout()
    def test9(self):
        for i in range(3):
            self.home.click_category(i)
            if i == 0:
                self.category.click_product("25")
            elif i == 1:
                self.category.click_product("16")
            elif i == 2:
                self.category.click_product("9")
            self.product.click_add_to_cart()
            self.product.click_back_to_home()
        self.home.click_shopping_cart_window()
        self.home.click_checkout()
        self.order_payment.enter_username("elad1234")
        self.order_payment.enter_password("Thbyrby145")
        self.order_payment.click_login()
        self.order_payment.click_next()
        self.order_payment.click_master_credit()
        self.order_payment.click_edit()
        self.order_payment.fill_master_card_details("123456789123","432","elad-ratner","2","4")
        self.order_payment.click_pay_now()

