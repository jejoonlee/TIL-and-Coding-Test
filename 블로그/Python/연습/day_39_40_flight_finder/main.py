# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from datetime import datetime, timedelta
from dateutil.relativedelta import *
from pprint import pprint

tomorrow = datetime.now() + timedelta(1)
sixmonths = tomorrow + relativedelta(months=+6)
tomorrow = tomorrow.strftime("%d/%m/%Y")
sixmonths = sixmonths.strftime("%d/%m/%Y")

data_manager = DataManager()
flight_search = FlightSearch()

# 구글 시트에 있는 정보를 갖고 온다
data_sheet = data_manager.get_destination_data()

# 정보 안에 내용을 수정을 한다
# DB 내에만 수정이 된 것. 구글 시트는 수정 되기 전이다
for index, data in enumerate(data_sheet):
    location_code = flight_search.get_destination_code(data["city"])
    data_sheet[index]["iataCode"] = location_code

# DB 내에서 수정한 데이터를, 구글 시트에 반영한
data_manager.update_destination_code()

for data in data_sheet:
    flight = flight_search.check_flight("ICN", data["iataCode"], tomorrow, sixmonths)
    price = (round(flight.price)//1000) * 1000
    print(data)

    if price < data["lowestPrice"]:
        content = f"비용 : {price}원 \nFrom : {flight.origin_city}-{flight.origin_airport} \nTo : {flight.destination_city}-{flight.destination_airport} \nOut : {flight.out_date} \nReturn : {flight.return_date}"

        email = NotificationManager()
        email.send_email("devjoon1996@gmail.com", content=content)
        print("email sent")
