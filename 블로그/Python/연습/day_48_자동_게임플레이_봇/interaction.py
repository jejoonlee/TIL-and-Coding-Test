from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, 'cookie')

timeout = time.time() + 5
five_min = time.time() + 60*5


item_name = ['Cursor', 'Grandma', 'Factory', 'Mine', 'Shipment', 'Alchemy lab', 'Portal', 'Time machine']

while True:
    cookie.click()

    if time.time() > timeout:

        all_price = []
        for item in item_name:
            item_price = driver.find_element(By.XPATH, f'//*[@id="buy{item}"]/b')
            price = int(item_price.text.split()[-1].replace(',', ''))
            all_price.append(price)

        money = driver.find_element(By.XPATH, '//*[@id="money"]')
        money = int(money.text)
        print(money)

        # 아이템 중 제일 비싼 아이템 사는 것
        for i in range(len(all_price) - 1, -1, -1):
            if money > all_price[i]:
                purchase = driver.find_element(By.XPATH, f'//*[@id="buy{item_name[i]}"]')
                purchase.click()
                break

        timeout = time.time() + 5

    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.XPATH, '//*[@id="cps"]')
        print(cookie_per_s.text)
        break

driver.quit()