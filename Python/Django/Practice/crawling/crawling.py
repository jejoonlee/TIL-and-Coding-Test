from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchWindowException
import csv

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메세지 없애기
chrome_options.add_experimental_option('excludeSwitches', ["enable-logging"])


chrome_options.add_argument('--start-maximized') #브라우저가 최대화된 상태로 실행됩니다.
chrome_options.add_argument("disable-infobars")

driver = webdriver.Chrome(options=chrome_options)

# csv 파일 생성
# csv 파일이 저장될 경로 / 모드 (쓰기 모드) / newline (윈도의 경우 줄바꿈이 자동으로 들어간다)
f = open("C:\\Users\\ADMIN\\OneDrive\\Desktop\\TIL\\Python\\Django\\Practice\\crawling\\card_data.csv", 'w', encoding='CP949', newline='')
card_data = csv.writer(f)

f2 = open("C:\\Users\\ADMIN\\OneDrive\\Desktop\\TIL\\Python\\Django\\Practice\\crawling\\benefit_data.csv", 'w', encoding='CP949', newline='')
benefit_data = csv.writer(f2)

card_id = 0
for i in range(1, 2435):
    # 카드 디테일 페이지를 하나씩 돌면서, 만약에 카드 디테일이 있으면 정보를 가지고 오고
    # 없으면 except: continue를 통해 넘어간다
    try:
        # 카드 고릴라의 URL에서 카드 디테일 페이지에서 첫 번째 카드를 가지고 온다
        driver.get(f"https://www.card-gorilla.com/card/detail/{i}")

        # 스크롤을 하다보면, 나오는 fixmenu를 안 보이도록 설정
        driver.execute_script('document.querySelector("#q-app > header").style.visibility="hidden";')

        # id를 만들어서 card_data 테이블과 benefit_data 테이블을 연결시킨다
        card_id += 1

        # 카드 이름 (꼭 있음)
        card_name = driver.find_element(By.CSS_SELECTOR, '#q-app > section > div.card_detail.fr-view > section > div > article.card_top > div > div > div.data_area > div.tit > strong')
        card_name = card_name.text

        # 카드사 (꼭 있음)
        card_brand = driver.find_element(By.CSS_SELECTOR, '#q-app > section > div.card_detail.fr-view > section > div > article.card_top > div > div > div.data_area > div.tit > p')
        card_brand = card_brand.text

        # 카드 이미지 (꼭 있음)
        card_image = driver.find_element(By.CSS_SELECTOR, '#q-app > section > div.card_detail.fr-view > section > div > article.card_top > div > div > div.card_img > img')
        card_image = card_image.get_attribute('src')

        
        # 카드 연회비
        card_in_out = driver.find_element(By.CSS_SELECTOR, '#q-app > section > div.card_detail.fr-view > section > div > article.card_top > div > div > div.data_area > div.bnf2 > dl:nth-child(1) > dd.in_out')
        card_in_out = card_in_out.text

        # 카드 실적
        card_record = driver.find_element(By.CSS_SELECTOR, '#q-app > section > div.card_detail.fr-view > section > div > article.card_top > div > div > div.data_area > div.bnf2 > dl:nth-child(2)')
        card_record = card_record.text

        try:
            # 카드 타입
            card_type = driver.find_element(By.CSS_SELECTOR, '#q-app > section > div.card_detail.fr-view > section > div > article.card_top > div > div > div.data_area > div.bnf2 > dl:nth-child(3) > dd')
            card_type = card_type.text
        except:
            NoSuchWindowException
            card_type = None


        print(f"card_name: {card_name}")
        print(f"card_brand: {card_brand}")
        print(f"card_in_out: {card_in_out}")
        print(f"card_image: {card_image}")
        print(f"card_record: {card_record}")
        print(f"card_type: {card_type}")
        card_data.writerow([card_id, card_name, card_brand, card_in_out, card_image, card_record, card_type])


        # =============== 카드 혜택 ==============================

        # CSS 지정자를 통해서, 혜택 이름들을 리스트로 가지고 온다 (나중에 .text를 통해서 문자로 변환한다)
        benefit_name = driver.find_elements(By.CSS_SELECTOR,'#q-app > section > div.card_detail.fr-view > section > div > article.cmd_con.benefit > div.lst.inner.faq_area > dl > dt > strong')
        benefit_content = driver.find_elements(By.CSS_SELECTOR, '#q-app > section > div.card_detail.fr-view > section > div > article.cmd_con.benefit > div.lst.inner.faq_area > dl > dt > i')

        benefit_click = driver.find_elements(By.CSS_SELECTOR, "#q-app > section.contentArea > div.card_detail.fr-view > section > div > article.cmd_con.benefit > div.lst.inner.faq_area > dl > dt")

        for i in range(len(benefit_name)):
            bnf_name = benefit_name[i].text
            bnf_content = benefit_content[i].text
            benefit_click[i].click()
            benefit_content_all = driver.find_elements(By.CSS_SELECTOR, "#q-app > section > div.card_detail.fr-view > section > div > article.cmd_con.benefit > div.lst.inner.faq_area > dl.on > dd > div")
            bnf_content_all = benefit_content_all[i].text
            print(bnf_name)
            print(bnf_content)
            print(bnf_content_all)
            benefit_data.writerow([card_id, bnf_name, bnf_content, bnf_content_all])
    
    except:
        continue

driver.quit()