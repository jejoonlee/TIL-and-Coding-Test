import requests
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
import time


MY_LAT = 37.172820
MY_LONG = 127.096149

def send_email():
    my_email = "devjoon1996@naver.com"
    my_password = "alex2006!"
    receiver = "jejoonlee@naver.com"

    connection = smtplib.SMTP_SSL("smtp.naver.com", port=465)
    connection.login(my_email, my_password)

    msg = MIMEText(f"Look above!")
    msg["From"] = my_email
    msg["Subject"] = "ISS above you"
    msg["To"] = receiver

    connection.sendmail(my_email, receiver, msg.as_string())
    connection.close()

def is_above():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT -5 <= iss_latitude <= MY_LAT -5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True
    else:
        return False

#Your position is within +5 or -5 degrees of the ISS position.

def is_night():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    if int(sunrise_hour) + 9 >= 24:
        sunrise_hour = (int(sunrise_hour) + 9) - 24

    if int(sunset_hour) + 9 >= 24:
        sunset_hour = (int(sunset_hour) + 9) - 24
    else:
        sunset_hour = int(sunset_hour) + 9

    time_now = datetime.now()

    if sunrise_hour <= time_now.hour <= sunset_hour:
        return False
    else:
        return True


# If the ISS is close to my current position

while True:
    time.sleep(60)
    
    iss_location = is_above()
    night = is_night()

    if iss_location == True and night == True:
        send_email()


# BONUS: run the code every 60 seconds.



