import requests
from datetime import datetime


# https://pixe.la/v1/users/harshaja/graphs/graph1.html


USERNAME = "USERNAME"
TOKEN = "USER_TOKEN"
GRAPH_ID = "GRAPH_ID"

# --------------Create an account ---------------------------------

pixel_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}
# response = requests.post(url=pixel_endpoint, json=user_params)
# print(response.text)


# --------------------------- Create a new  graph with different ID--------------------------------------


graph_endpoint = f"{pixel_endpoint}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": TOKEN
}

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "hours",
    "type": "float",
    "color": "ajisai",
}


# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# ---------------------------------- POST the data in pixela---------------------------------------------

post_graph = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime(year=2022, month=1, day=20)


post_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10",
}

# response = requests.post(url=post_graph, json=post_params, headers=headers)
# print(response.text)


# ------------------------------- Update the Pixela------------------------------------------

update_endpoint = f"{post_graph}/20220120"

new_pixela_data = {
    "quantity": "1.6"
}

# response = requests.put(url=update_endpoint, json=new_pixela_data, headers=headers)
# print(response.text)


# --------------------------- Delete the pixela ----------------------------------------

delete_endpoint = f"{post_graph}/20220120"
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)

