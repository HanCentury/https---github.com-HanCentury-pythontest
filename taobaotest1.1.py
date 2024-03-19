import csv
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from os import path

def scrape_page(driver, data):
    goods = driver.find_elements(By.XPATH,'//div[@class="grid g-clearfix"]/div/div')
    for good in goods:
        # Get product link
        link = good.find_element(By.XPATH, './div[2]/div[@class="row row-2 title"]/a').get_attribute('href').strip()
        # Get product title
        title=good.find_element(By.XPATH, './/div[@class="row row-2 title"]/a').text
        # Get product price
        price = good.find_element(By.XPATH,'.//strong').text + '元'  
        # Get product review count
        commit = good.find_element(By.XPATH,'.//div[@class="deal-cnt"]').text
        shop= good.find_element(By.XPATH,'.//div[@class="shop"]/a/span[2]').text  # 店铺名称  # 手写
        good_data = {
            'Product Title': title,
            'Product Price': price,
            'Product Link': link,
            'Review Count': commit,
            'Shop': shop
        }
        data.append(good_data)

def main(pages):
    url = 'https://www.taobao.com/'
    want = input('请输入你要搜索的商品：')
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(30)
    input_search = driver.find_element(By.ID, 'q')
    input_search.send_keys(want)
    input_search.send_keys(Keys.ENTER)
    sleep(10)  # Adjust this wait time as necessary

    data = []
    scrape_page(driver, data)

    # Pagination
    page = 1
    while page < pages:
        try:
            next_button = driver.find_element_by_css_selector('.next')  # Locate the next page button
            next_button.click()
            sleep(5)  # Adjust this wait time as necessary
            scrape_page(driver, data)
            page += 1
        except:
            break

    file_path = path.join('product_data.csv')
    # Append product data to the file
    header = ['Product Title', 'Product Price', 'Product Link', 'Review Count', 'Shop']
    with open(file_path, 'a+', encoding='utf-8', newline='') as wf:
        csv_writer = csv.DictWriter(wf, header)
        # Write header if file is empty
        if wf.tell() == 0:
            csv_writer.writeheader()
        # Write data
        csv_writer.writerows(data)

    driver.quit()

if __name__ == "__main__":
    num_pages = int(input('请输入要抓取的页面数量：'))
    main(num_pages)
