import csv

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from os import path

url = 'https://www.baidu.com/'
want = input('请输入需要查询的商品\n')
driver = webdriver.Edge()
driver.get(url)
driver.implicitly_wait(3)
input_search = driver.find_element(By.ID,'kw')
input_search.send_keys(want)
input_search.send_keys(Keys.ENTER)
sleep(40)