import csv
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from os import path

def scrape_page(driver, data):
    goods = driver.find_elements(By.CLASS_NAME, 'gl-item')
    for good in goods:
        link = good.find_element(By.TAG_NAME, 'a').get_attribute('href')
        title = good.find_element(By.CSS_SELECTOR, '.p-name em').text.replace('\n', '')
        price = good.find_element(By.CSS_SELECTOR, '.p-price strong').text.replace('\n', '')
        commit = good.find_element(By.CSS_SELECTOR, '.p-commit a').text.replace('\n', '')
        shop = good.find_element(By.CSS_SELECTOR, '.p-shop a').text
        good_data = {
            'Product Title': title,
            'Product Price': price,
            'Product Link': link,
            'Review Count': commit,
            'Shop': shop
        }
        data.append(good_data)

def main(url,pages,want):
    #url = 'https://search.jd.com/'
    driver = webdriver.Edge()
    driver.get(url)
    driver.implicitly_wait(3)
    input_search = driver.find_element(By.ID, 'keyword')
    input_search.send_keys(want)
    input_search.send_keys(Keys.ENTER)
    sleep(40)  # Adjust this wait time as necessary

    data = []
    scrape_page(driver, data)

    # Pagination
    page = 1
    while page < pages:
        try:
            next_button = driver.find_element(By.CSS_SELECTOR, '.pn-next')  # Locate the next page button
            next_button.click()
            sleep(5)  # Adjust this wait time as necessary
            scrape_page(driver, data)
            page += 1
        except:
            break

    file_path = path.join('product_data.csv')
    # Append product data to the file
    header = ['Product Title', 'Product Price', 'Product Link', 'Review Count', 'Shop']
    with open(file_path, 'a+', encoding='ANSI', newline='') as wf:
        csv_writer = csv.DictWriter(wf, header)
        # Write header if file is empty
        if wf.tell() == 0:
            csv_writer.writeheader()
        # Write data
        csv_writer.writerows(data)

    driver.quit()

if __name__ == "__main__":
    url=input("你想要搜索的网址")
    want = input('请输入你要寻找的物品名称: ')
    num_pages = int(input('请选择你要查找的页数范围: '))
    main(url,num_pages,want)
