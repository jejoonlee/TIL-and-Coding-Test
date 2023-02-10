import requests
from pprint import pprint
import os
import dotenv

dotenv.load_dotenv()



class DataManager:
    #This class is responsible for talking to the Google Sheet.
    
    def __init__(self):
        self.destination_data = {}

        sheet_token = os.getenv("sheet_token")
        self.bearer_header = {
            "Authorization": f"Bearer { sheet_token }",
        }

    def get_destination_data(self):

        sheet_response = requests.get(url=os.getenv("sheet_endpoint"), headers=self.bearer_header)

        self.destination_data = sheet_response.json()['prices']

        return self.destination_data

    def update_destination_code(self):

        for city in self.destination_data:
            new_data = {
                "price" :{
                   "iataCode" : city["iataCode"], 
                }
            }

            sheet_update = requests.put(url=f'{os.getenv("sheet_endpoint")}/{city["id"]}', json=new_data,headers=self.bearer_header)
            sheet_update.raise_for_status()