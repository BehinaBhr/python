# TODO: Make a request to the forecast API using the requests module.
#  Print out the HTTP status code that you get back. Print the response to the console.
#  Copy-paste the response to an online JSON viewer (e.g., jsonviewer.stack.hu).
#  Locate the weather id and description for each forecast.


import requests
from twilio.rest import Client

account_sid = "ACaa0365418ab81d7e959a8e14cce3f9ac"
auth_token = "b256b2f39c056f6b01f9a7abc35b1f4e"


MY_API_KEY = "44841eb74c3749b00d55eda33a6e0494"
MY_Latitude = 49.276661
MY_Longitude = -122.866798
# https://api.openweathermap.org/data/2.5/weather?lat=49.276661&lon=-122.866798&appid=44841eb74c3749b00d55eda33a6e0494
parameters = {"lat": 49.276661, "lon": -122.866798, "appid": MY_API_KEY, "cnt": 4}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
print(response)
response.raise_for_status()
weather_data = response.json()

# for hour_data in weather_data['list']:
#     condition_code = hour_data['weather'][0]["id"]
#     if int(condition_code) < 700:
#         print("Bring an umbrella.")

will_rain = False
for hour_data in weather_data['list']:
    condition_code = hour_data['weather'][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    # print("Bring an umbrella.")
    client = Client(account_sid, auth_token)
    message = client.messages.create(from_='+18509990952',
                                     body="It's going to rain today. Remember to bring an umbrella ☔️",
                                     to='+17788757291')
    print(message.status)
