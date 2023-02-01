import requests
from datetime import datetime

# response = requests.get(url="http://api.open-notify.org/iss-now.json")

# # 모든 에러 요인을 알려준
# response.raise_for_status()

# # 응답을 json 형태로 바꾸는 것
# data = response.json()

# lat = data["iss_position"]["latitude"]
# long = data["iss_position"]["longitude"]


#------------ sunset, sunrise -------------------
MY_LAT = 37.172820
MY_LONG = 127.096149

parameter = {
    "lat" : MY_LAT,
    "lng" : MY_LONG,
    "formatted" : 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameter)
# https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400

response.raise_for_status()

data = response.json()

sunrise_hour = data['results']['sunrise'].split("T")[1].split(":")[0]
sunset_hour = data['results']['sunset'].split("T")[1].split(":")[0]

if int(sunrise_hour) + 9 >= 24:
    sunrise_hour = (int(sunrise_hour) + 9) - 24

if int(sunset_hour) + 9 >= 24:
    sunset_hour = (int(sunset_hour) + 9) - 24
else:
    sunset_hour = int(sunset_hour) + 9


print(sunrise_hour)
print(sunset_hour)

time_now = datetime.now()
print(time_now.hour)