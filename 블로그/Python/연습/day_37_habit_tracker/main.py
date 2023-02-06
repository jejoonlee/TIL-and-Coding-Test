import requests
import os
import dotenv
from datetime import datetime

dotenv.load_dotenv()

USERNAME = "jejoonlee"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
parameter = {
    "token": os.getenv("pixela_token"), 
    "username": USERNAME, 
    "agreeTermsOfService":"yes", 
    "notMinor":"yes"
}

# response = requests.post(url=pixela_endpoint, json=parameter)
# print(response.text)

pixela_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_parameter = {
    "id" : GRAPH_ID,
    "name" : "Coding Study",
    "unit" : "commit",
    "type" : "int",
    "color": "sora",
    "timezone": "Asia/Seoul",
}

headers = {
    "X-USER-TOKEN" : os.getenv("pixela_token"),
}

# graph_response = requests.post(url=pixela_graph_endpoint, json=graph_parameter, headers=headers)
# print(graph_response.text)

#------------------ 커밋 넣기 ----------------------
today = datetime.now()

pixela_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_parameter = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10",
}

pixel_response = requests.post(url=pixela_pixel_endpoint, json=pixel_parameter, headers=headers)
print(pixel_response.text)


#--------------- 커밋 바꾸기 -----------------------

p_change = {
    "quantity": "5"
}

change_response = requests.put(url=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20230206", json=p_change, headers=headers)
print(change_response.text)