import csv

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from os import path

url = 'https://www.taobao.com/'
want = input('请输入需要查询的商品\n')
driver = webdriver.Edge()
driver.get(url)
driver.implicitly_wait(3)
input_search = driver.find_element(By.ID,'q')
input_search.send_keys(want)
input_search.send_keys(Keys.ENTER)
sleep(40)
data=[]
goods = driver.find_elements(By.CLASS_NAME,'Card--doubleCardWrapper--L2XFE73')
for good in goods:
    # 获取商品链接
    link = good.find_element(By.TAG_NAME,'a').get_attribute('href')
    # 获取商品标题名称
    title = good.find_element(By.CSS_SELECTOR,'.Title--descWrapper--HqxzYq0').text.replace('\n', '')
    # 获取商品价格
    price = good.find_element(By.CSS_SELECTOR,'.Price--priceWrapper--Q0Dn7pN ').text.replace('\n', '')
    # 获取商品评价数量
    commit = good.find_element(By.CSS_SELECTOR,'.Price--realSales--FhTZc7U').text.replace('\n', '')  
    shop = good.find_element(By.CSS_SELECTOR,'.ShopInfo--TextAndPic--yH0AZfx').text
    good_data = {
        '商品标题': title,
        '商品价格': price,
        '商品链接': link,
        '评论量': commit,
        '店铺': shop
    }   
    data.append(good_data)
file_path = path.join('taobaogood.csv')
# 以追加写入的方式将商品数据保存到文件中
header = ['商品标题', '商品价格', '商品链接', '评论量','店铺']
with open(file_path, 'a+', encoding='ANSI', newline='') as wf:
    f_csv = csv.DictWriter(wf, header)
    # 检查文件是否存在，如果不存在则写入表头
    if wf.tell() == 0:
        f_csv.writeheader()
    # 写入数据
    f_csv.writerows(data)
