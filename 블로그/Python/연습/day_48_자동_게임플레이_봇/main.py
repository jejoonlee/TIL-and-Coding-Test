from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.python.org/")

upcomming_event = {}


time = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/time')
name = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/a')

for i in range(len(time)):
    upcomming_event[i] = {
        'time' : time[i].text,
        'name' : name[i].text,
    }

driver.quit()

print(upcomming_event)