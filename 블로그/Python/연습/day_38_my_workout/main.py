import requests
import os
import dotenv
from datetime import datetime

dotenv.load_dotenv()

endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.getenv("sheet_endpoint")

header = {
    "x-app-id" : os.getenv("APPID"),
    "x-app-key" : os.getenv("nutritionix_api_key"),
}

exercise = input("Tell me which exercises you did: ").lower()

parameter = {
    "query": exercise,
    "gender" : "MALE",
    "age" : 27,
    "height_cm" : 170,
    "weight_kg" : 70,
}

response = requests.post(url=endpoint, json=parameter, headers=header)
response.raise_for_status()

workout_list = response.json()['exercises']


now = datetime.now()

now_date = now.strftime("%Y/%m/%d")
now_time = now.strftime("%X")

bearer_headers = {
    "Authorization": f"Bearer {os.environ['token']}"
}


for workout in workout_list:
    sheet_input = {
        "workout": {
            "date": now_date,
            "time": now_time,
            "exercise": workout["name"].title(),
            "duration": int(workout["duration_min"]),
            "calories": workout["nf_calories"],
        }  
    }

    sheet_response = requests.post(url=os.getenv("sheet_endpoint"), json=sheet_input, headers=bearer_headers)

    print(sheet_response.text)
