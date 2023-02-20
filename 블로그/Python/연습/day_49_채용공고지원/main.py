import os
import dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

dotenv.load_dotenv()

my_email = os.getenv("email")
my_password = os.getenv("password")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.linkedin.com/home")

email = driver.find_element(By.XPATH, '//*[@id="session_key"]')
password = driver.find_element(By.XPATH, '//*[@id="session_password"]')
login = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/form/button')

email.send_keys(my_email)
password.send_keys(my_password)
login.click()

time.sleep(5)
search = driver.find_element(By.XPATH, '//*[@id="global-nav-typeahead"]/input')

search.send_keys("python developer")
search.send_keys(Keys.ENTER)

time.sleep(3)
job_button = driver.find_element(By.XPATH, '//*[@id="search-reusables__filters-bar"]/ul/li[1]/button')
job_button.click()

time.sleep(3)
experience = driver.find_element(By.XPATH, '//*[@id="search-reusables__filters-bar"]/ul/li[4]')
experience.click()

# time.sleep(3)
# intern = driver.find_element(By.XPATH, '//*[@id="artdeco-hoverable-artdeco-gen-52"]/div[1]/div/form/fieldset/div[1]/ul/li[1]/label')
# new = driver.find_element(By.XPATH, '//*[@id="artdeco-hoverable-artdeco-gen-52"]/div[1]/div/form/fieldset/div[1]/ul/li[2]/label')
# experience_confirm = driver.find_element(By.XPATH, '//*[@id="ember122"]')

# intern.click()
# new.click()
# experience_confirm.click()


time.sleep(3)
jobs = driver.find_element(By.XPATH, '//*[@id="ember1644"]/div/div[1]')
save = driver.find_element(By.XPATH, '//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/button')

jobs.click()
save.click()

driver.quit()