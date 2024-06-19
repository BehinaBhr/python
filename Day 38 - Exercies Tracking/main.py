import requests
from datetime import datetime

APP_ID = "5d94a273"
API_KEY = "0b8b1dcb1b80ce1ebdd5c6ea20d73de2"
NLE_END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_USERNAME = "BeBhr"
SHEETY_PASSWORD = "Behi4877"
GOOGLE_SHEET_NAME = "workout"
SHEETY_END_POINT = "https://api.sheety.co/f3fd64781ef5e3f27c277d9dcf70e696/workoutTracking/workouts"
SHEETY_TOKEN = "123thisissecret456"


GENDER = "female"
WEIGHT_KG = 62
HEIGHT_CM = 162
AGE = 25
exercise = input("Tell me which exercises you did: ")

user_parameters = {"query": exercise, "gender": GENDER,
                   "weight_kg": WEIGHT_KG, "height_cm": HEIGHT_CM,
                   "age": AGE}


headers = {"x-app-id": APP_ID, "x-app-key": API_KEY}


response = requests.post(NLE_END_POINT, json=user_parameters, headers=headers)
result = response.json()
print(f"Nutritionix API call: \n {result} \n")


now_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {GOOGLE_SHEET_NAME: {"date": now_date,
                                        "time": now_time,
                                        "exercise": exercise["name"].title(),
                                        "duration": exercise["duration_min"],
                                        "calories": exercise["nf_calories"]}}

    # # # No Auth
    # (Make sure change the Sheety's authentication to no code and save changes)
    # https://dashboard.sheety.co/projects/6570f8efec339004d7c486c0/auth
    sheet_response = requests.post(SHEETY_END_POINT, json=sheet_inputs)

    # # # Basic Auth
    # sheet_response = requests.post(SHEETY_END_POINT, json=sheet_inputs,
    #                                auth=(SHEETY_USERNAME, SHEETY_PASSWORD))

    # # # Bearer Token
    # bearer_headers = {"Authorization": f"Bearer {SHEETY_TOKEN}"}
    # sheet_response = requests.post(SHEETY_END_POINT, json=sheet_inputs,
    #                                headers=bearer_headers)

    print(f"Sheety Response: \n {sheet_response.text}")

