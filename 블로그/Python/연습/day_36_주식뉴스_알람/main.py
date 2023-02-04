import requests
import os
import dotenv
from datetime import datetime, timedelta

dotenv.load_dotenv()

SEARCH = "nike"
STOCK = []

parameter = {
    "function": "SYMBOL_SEARCH",
    "keywords" : SEARCH,
    "apikey": os.getenv("api_key"),
}

symbol_response = requests.get(url="https://www.alphavantage.co/query", params=parameter)
symbol_response.raise_for_status()

symbol_data = symbol_response.json()["bestMatches"]

if symbol_data:
    for data in symbol_data:
        if data["4. region"] == "United States":
            STOCK.append(data["1. symbol"])

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

today = datetime.now().weekday()
yesterday = (datetime.now() - timedelta(1)).date()
yesterday_2 = (datetime.now() - timedelta(2)).date()

if today == 6:
    yesterday = (datetime.now() - timedelta(2)).date()
    yesterday_2 = (datetime.now() - timedelta(3)).date()
elif today == 0:
    yesterday = (datetime.now() - timedelta(3)).date()
    yesterday_2 = (datetime.now() - timedelta(4)).date()

elif today == 1:
    yesterday_2 = (datetime.now() - timedelta(4)).date()

y_year, y_month, y_day = yesterday.year, "{:02d}".format(yesterday.month), "{:02d}".format(yesterday.day)
y2_year, y2_month, y2_day = yesterday_2.year, "{:02d}".format(yesterday_2.month), "{:02d}".format(yesterday_2.day)

yesterday = f"{y_year}-{y_month}-{y_day}"
yesterday_2 = f"{y2_year}-{y2_month}-{y2_day}"


for stock in STOCK:
    parameter = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol" : stock,
        "apikey": os.getenv("api_key"),
    }

    response = requests.get(url="https://www.alphavantage.co/query", params=parameter)
    response.raise_for_status()
    stock_data = response.json()["Time Series (Daily)"]

    data_list = [value for (key,value) in stock_data.items()]


    close_value_1 = float(data_list[0]["4. close"])
    close_value_2 = float(data_list[1]["4. close"])

    change = (close_value_1 - close_value_2) // close_value_1

    if abs(change) >= 1:
        if change < 0:
            change = f"🔻 {abs(change)}%"
        else:
            change = f"🔺 {abs(change)}%"



## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

    news_parameter = {
        "apiKey": os.getenv("news_api_key"),
        "q": stock,
        "language": "en",
        "sortBy": "popularity",
        "from": yesterday,
        "to": yesterday_2,
    }

    news = requests.get(url="https://newsapi.org/v2/everything", params=news_parameter)
    news.raise_for_status()
    news_data = news.json()["articles"][:3]

    for news in news_data:
        print(news["title"])
        print(news["description"])



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

