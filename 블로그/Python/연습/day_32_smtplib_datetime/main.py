import pandas
import datetime as dt
import random
import smtplib
from email.mime.text import MIMEText

def send_email(receiver,letter):
    my_email = "devjoon1996@naver.com"
    my_password = "alex2006!"

    connection = smtplib.SMTP_SSL("smtp.naver.com", 465)
    connection.login(my_email, my_password)

    msg = MIMEText(letter)
    msg["From"] = my_email
    msg["Subject"] = "Happy Birthday!"
    msg["To"] = receiver

    connection.sendmail(my_email, receiver, msg.as_string())
    connection.close()

birthdays = pandas.read_csv("birthdays.csv")
today = dt.datetime.now()

names = {}
for index, birthday in birthdays.iterrows():
    if birthday["month"] == today.month and birthday["day"] == today.day:
        names[birthday["name"]] = birthday["email"]

letter_num = random.randint(1,3)

with open(f"letter_templates/letter_{letter_num}.txt") as data:
    letter = data.read()

for key, value in names.items():
    letter_to_send = letter.replace("[NAME]", key)

    send_email(receiver=value, letter=letter_to_send)