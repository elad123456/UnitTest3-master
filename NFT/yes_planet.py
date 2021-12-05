from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from unittest import TestCase
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


service1 = Service(r"C:\Users\Admin\Documents\ELAD\chromedriver.exe")
driver = webdriver.Chrome(service=service1)
driver.get("https://www.yesplanet.co.il/cinemas/rishon_letziyon/1072#/buy-tickets-by-cinema?in-cinema=1072&at=2021-12-03&view-mode=list")
driver.maximize_window()
driver.implicitly_wait(10)
wait=WebDriverWait(driver,10)
ishur_button = driver.find_element(By.ID,"consent_prompt_submit")
ishur_button.click()
moviestitle = driver.find_elements(By.CSS_SELECTOR,"[class='qb-movie-details col-sm-9 col-md-10 pull-right']>div>a")
movie="בית הסיוטים"
number_of_movie=-1
counter=0
for element in moviestitle:
    if movie in element.get_attribute("title"):
        number_of_movie=counter
        break
    counter+=1
movies = driver.find_elements(By.CSS_SELECTOR,"[class='qb-movie-details col-sm-9 col-md-10 pull-right']")
relevantmovie = movies[number_of_movie]
relevanthour = '00:20'
hours = relevantmovie.find_elements(By.CSS_SELECTOR,"[class='btn btn-primary btn-lg']")
for element in hours:
    if relevanthour == element.text:
        element.click()
rnumberoftickets = '3'
numberoftickets = driver.find_element(By.ID,"ddQunatity_0")
selectnumoftick = Select(numberoftickets)
selectnumoftick.select_by_value(rnumberoftickets)
order = driver.find_element(By.ID,"lbSelectSeats")
order.click()
canv = driver.find_element(By.CSS_SELECTOR, 'div>#SeatPlanContainer')
canvas_demantion = canv.size
canvas_center_x = canvas_demantion['width']//2
canvas_center_y = canvas_demantion['height']//2
print(canvas_center_x,canvas_center_y)
print(canvas_demantion)
driver.execute_script("arguments[0].scrollIntoView();",canv)
ActionChains(driver).move_to_element_with_offset(canv,0,0).click()

sleep(3)
driver.close()
