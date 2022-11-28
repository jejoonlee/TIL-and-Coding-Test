from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메세지 없애기
chrome_options.add_experimental_option('excludeSwitches', ["enable-logging"])

driver = webdriver.Chrome(options=chrome_options)

# for i in range(1, 2435): 
#     driver.get(f"https://www.card-gorilla.com/card/detail/{i}")
    
#     # 위에 URL의 HTML template에 CSS 지정자를 가지고 온다
#     card_name = driver.find_element(By.CSS_SELECTOR, ".card")
#     card_brand = driver.find_element(By.CSS_SELECTOR, ".brand")

#     print(i, card_name, card_brand, type(card_name))

# 카드 고릴라의 URL에서 카드 디테일 페이지에서 첫 번째 카드를 가지고 온다
driver.get(f"https://www.card-gorilla.com/card/detail/1")

# CSS 지정자를 통해서, 혜택 이름들을 리스트로 가지고 온다 (나중에 .text를 통해서 문자로 변환한다)
benefit_name = driver.find_elements(By.CSS_SELECTOR,'#q-app > section > div.card_detail.fr-view > section > div > article.cmd_con.benefit > div.lst.inner.faq_area > dl > dt > strong')
benefit_content = driver.find_elements(By.CSS_SELECTOR, '#q-app > section > div.card_detail.fr-view > section > div > article.cmd_con.benefit > div.lst.inner.faq_area > dl > dt > i')

benefit_click = driver.find_elements(By.CSS_SELECTOR, "#q-app > section > div.card_detail.fr-view > section > div > article.cmd_con.benefit > div.lst.inner.faq_area > dl > dt")

fixmenu = driver.find_element(By.CSS_SELECTOR, "#q-app > header > div.fixmenu_wrap.card_info")

print(benefit_click)


for i in range(len(benefit_name)):
    if fixmenu:
        
        bnf_name = benefit_name[i].text
        bnf_content = benefit_content[i].text
        benefit_click[i].click()
        print(f"======={i + 1}==============")
        print(bnf_name)
        print(bnf_content)
    else:
        bnf_name = benefit_name[i].text
        bnf_content = benefit_content[i].text
        benefit_click[i].click()
        print(f"======={i + 1}==============")
        print(bnf_name)
        print(bnf_content)

driver.quit()