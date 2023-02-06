import requests
import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()

def send_email():
    my_email = os.getenv("my_email")
    receive = "devjoon1996@gmail.com"
    my_password = os.getenv("my_password")

    connection = smtplib.SMTP_SSL(url="smtp.naver.com", port=465)
    connection.login(my_email, my_password)

    msg = MIMEText("12시간 안에 비가 오니 우산 챙겨!")
    msg["From"] = my_email
    msg["Subject"] = "오늘 비가 와요"
    msg["To"] = receive

    connection.sendmail(my_email, receive, msg.as_string())

api_key = os.getenv("api_key")

parameter = {
    "lat" : 37.190751,
    "lon": 127.078045,
    "appid": api_key,
    "exclude": "current, minutely, daily"
}

response = requests.get(url="https://api.openweathermap.org/data/3.0/onecall", params=parameter)

response.raise_for_status()

weather = response.json()["hourly"][0:12]

will_rain = False

for weather_hour in weather:
    condition_code = weather_hour["weather"][0]["id"]

    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    send_email()

print("weather check finished")