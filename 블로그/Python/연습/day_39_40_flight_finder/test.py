# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint

# data_manager = DataManager()
# location = FlightSearch()

# # 구글 시트에 있는 정보를 갖고 온다
# data_sheet = data_manager.get_destination_data()

# # 정보 안에 내용을 수정을 한다
# # DB 내에만 수정이 된 것. 구글 시트는 수정 되기 전이다
# for index, data in enumerate(data_sheet):
#     if data["iataCode"] == "":
#         location_code = location.get_destination_code(data["city"])
#         data_sheet[index]["iataCode"] = location_code

# # DB 내에서 수정한 데이터를, 구글 시트에 반영한
# data_manager.update_destination_code()

import requests
import os
import dotenv
from datetime import datetime, timedelta
from dateutil.relativedelta import *

dotenv.load_dotenv()

tomorrow = datetime.now() + timedelta(1)
sixmonths = tomorrow + relativedelta(months=+6)

header = {"apikey": os.getenv("flight_header")}

parameter = {
    "fly_from": "ICN",
    "fly_to": "TYO",
    "date_from": tomorrow.strftime("%d/%m/%Y"),
    "date_to": sixmonths.strftime("%d/%m/%Y"),
    "curr": "KRW",
    "nights_in_dst_from": 7,
    "nights_in_dst_to": 28,
    "flight_type": "round",
    "max_stopovers": 0,
}

response = requests.get(
    url="https://api.tequila.kiwi.com/v2/search", params=parameter, headers=header
)

flight_data = response.json()["data"]

# for data in flight_data:
#     print(f'{data["cityTo"]}: {round(data["price"])}원')
