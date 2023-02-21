from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import os
import dotenv
import time

dotenv.load_dotenv()

my_email = os.getenv("fb_email")
my_password = os.getenv("fb_password")

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://tinder.com/")
time.sleep(2)

#---- login ----
login_btn = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]')
login_btn.click()

#---- facebook ----
time.sleep(2)

fb_login_btn = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]/div/div')
fb_login_btn.click()

time.sleep(2)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]

driver.switch_to.window(fb_login_window)

fb_email = driver.find_element(By.CSS_SELECTOR, "#email")
fb_email.send_keys(my_email)

fb_password = driver.find_element(By.CSS_SELECTOR, "#pass")
fb_password.send_keys(my_password)

fb_login_click = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]')
fb_login_click.click()

driver.switch_to.window(base_window)

time.sleep(5)

location_allow = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div/div[3]/button[1]/div[2]')
location_allow.click()

alarm_disallow =driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div/div[3]/button[2]/div[2]')
alarm_disallow.click()

personal_info = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button/div[2]')
personal_info.click()

while True:
    time.sleep(3)
    like = driver.find_element(By.XPATH, '//*[@id="c-1351236777"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button')
    like.click()
    print("click")