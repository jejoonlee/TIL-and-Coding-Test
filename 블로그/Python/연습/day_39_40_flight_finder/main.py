#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from pprint import pprint
import os
import dotenv

dotenv.load_dotenv()

sheet_token = os.getenv("sheet_token")

bearer_header = {
    "Authorization": f"Bearer { sheet_token }",
}

sheet_response = requests.get(url=os.getenv("sheet_endpoint"), headers=bearer_header)

sheet_data = sheet_response.json()['prices']

for data in sheet_data:
    data['iataCode'] = "Testing"

pprint(sheet_data)