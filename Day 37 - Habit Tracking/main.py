import requests
import datetime

USERNAME = "be7bhr"
TOKEN = "123thisissecret4567"
GRAPH_ID = "graph2"

pixela_endpoint = "https://pixe.la/v1/users"
user_parameters = {"token": TOKEN, "username": USERNAME,
                   "agreeTermsOfService": "yes", "notMinor": "yes"}
# STEP_1
# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

# STEP_2
graph_endpoint = f"https://pixe.la//v1/users/{USERNAME}/graphs"

graph_config = {"id": GRAPH_ID, "name": "English Graph", "unit": "minuet",
                "type": "int", "color": "ajisai"}

headers = {"X-USER-TOKEN": TOKEN}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# STEP_3
# Type in browser f"https://pixe.la//v1/users/{USERNAME}/graphs/{GRAPH_ID}"
# ->  https://pixe.la/v1/users/be7bhr/graphs/graph2.html

# STEP_4
pixel_creation_endpoint = f"https://pixe.la//v1/users/{USERNAME}/graphs/{GRAPH_ID}"

# today:
# date = datetime.datetime.now()
# different_time:
date = datetime.datetime(year=2023, month=11, day=3)

THE_DAY = date.strftime('%Y%m%d')

# pixel_data = {"date": THE_DAY, "quantity": input("How many minutes did you study in this day?")}
# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

# STEP_5
update_endpoint = f"https://pixe.la//v1/users/{USERNAME}/graphs/{GRAPH_ID}/{THE_DAY}"
update_config = {"quantity": "2"}

# response = requests.put(url=update_endpoint, json=update_config, headers=headers)
# print(response.text)

# STEP_6
delete_endpoint = f"https://pixe.la//v1/users/{USERNAME}/graphs/{GRAPH_ID}/{THE_DAY}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)