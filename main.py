import requests
from datetime import datetime

USERNAME = "Your_pixel_user_name"
TOKEN = "Your_pixel_Token"
ID = "graph1"
TODAY = datetime.now().strftime("%Y%m%d")

param = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
pixel = "https://pixe.la/v1/users"
# response = requests.post(url=pixel, json=param)
# print(response.text)

graph_endpoint = f"{pixel}/{USERNAME}/graphs"
header = {
    "X-USER-TOKEN": TOKEN
}
body = {
    "id": ID,
    "name": "Coding Graph",
    "unit": "Minutes",
    "type": "int",
    "color": "kuro"
}
# response = requests.post(url=graph_endpoint, headers=header, json=body)
# print(response.text)

post_pixel = f"{graph_endpoint}/{ID}"
config_pixel = {
    "date": TODAY,
    "quantity": "120",
}

# response = requests.post(url=post_pixel, json=config_pixel, headers=header)
# print(TODAY.strftime("%Y%m%d"))

update_pixel = f"{post_pixel}/{TODAY}"
config_update_pixel = {
    "quantity": "180",
}
response = requests.put(url=update_pixel, json=config_update_pixel, headers=header)
print(response.text)
