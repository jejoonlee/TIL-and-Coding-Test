import smtplib
from email.mime.text import MIMEText
import datetime as dt
import random

def send_email(content):
    my_email = "devjoon1996@naver.com"
    my_password = "alex2006!"
    receive = "jejoonlee@naver.com"

    connection = smtplib.SMTP_SSL("smtp.naver.com", 465)
    connection.login(my_email, my_password)

    msg = MIMEText(content)
    msg['From'] = my_email
    msg['Subject'] = "월요일 명언"
    msg['To'] = receive

    connection.sendmail(my_email, receive, msg.as_string())
    connection.close()

def get_quotes():
    with open("quotes.txt") as data_file:
        quotes = data_file.read().split('\n')
        quote = random.choice(quotes)
    return quote

now = dt.datetime.now()

if now.weekday() == 0:
    quote = get_quotes()
    send_email(quote)
    print(quote)



# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()

# print(now.year)
