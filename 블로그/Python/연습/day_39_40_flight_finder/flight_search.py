import requests
import os
import dotenv
from flight_data import FlightData

dotenv.load_dotenv()

class FlightSearch:

    def __init__(self):
        self.header = {
            "apikey" : os.getenv("flight_header")
        }

    def get_destination_code(self, city_name):
        parameter = {
            "term" : city_name,
        }

        response = requests.get(url="https://api.tequila.kiwi.com/locations/query", headers=self.header, params=parameter)
        response.raise_for_status()
        code = response.json()["locations"][0]["code"]

        return code

    def check_flight(self, fly_from, fly_to, date_from, date_to):
        parameter = {
            "fly_from" : fly_from,
            "fly_to" : fly_to,
            "date_from" : date_from,
            "date_to": date_to,
            "curr": "KRW",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "max_stopovers" : 0,
        }

        response = requests.get(url="https://api.tequila.kiwi.com/v2/search", params=parameter, headers=self.header)

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flight to {fly_to} from {fly_from} is available")
            return None

        flight_data = FlightData(
            price = data["price"],
            origin_city= data["route"][0]["cityFrom"],
            origin_airport= data["route"][0]["flyFrom"],
            destination_city= data["route"][0]["cityTo"],
            destination_airport= data["route"][0]["flyTo"],
            out_date= data["route"][0]["local_departure"].split("T")[0],
            return_date= data["route"][1]["local_departure"].split("T")[0],
        )


        return flight_data