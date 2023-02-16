
from send_email import SendEmail
from bs4 import BeautifulSoup
import requests

url = "https://www.amazon.com/Nike-Jordan-Shoes-Cement-White-true/dp/B0BT3X9D4W/ref=sr_1_80?qid=1676525528&s=fashion-mens-intl-ship&sr=1-80&th=1"

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Accept-Language" : "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6,de;q=0.5,fr;q=0.4",
    "Cookie": "COOKIE INFO from csm-hit field",
    'Accept-Encoding':'gzip, deflate',
    'Connection':'keep-alive',
    'Upgrade-Insecure-Requests':'1',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.amazon.com/',
}

response = requests.get(url, headers=headers)
response.raise_for_status()

website = response.text

# print(website)

soup = BeautifulSoup(website, "lxml")
print(soup.prettify())
