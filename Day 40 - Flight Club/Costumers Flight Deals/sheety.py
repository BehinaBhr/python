import requests

SHEETY_USERNAME = "BeBhr"
SHEETY_PASSWORD = "Behi4877"
SHEETY_END_POINT = "https://api.sheety.co/f3fd64781ef5e3f27c277d9dcf70e696/flightDeals/users"

# No Auth:
def post_new_row(name, last_name, email):
    sheet_inputs = {"user": {"firstName": name,
                       "lastName": last_name,
                       "email": email}}
    response = requests.post(SHEETY_END_POINT, json=sheet_inputs)
    response.raise_for_status()
    print(response.text)
    
# Bearer Token:
# SHEETY_TOKEN = "123thisissecret456"
# def post_new_row(first_name, last_name, email):
#     headers = {"Authorization": f"Bearer {SHEETY_TOKEN}",
#         "Content-Type": "application/json"}

#     sheet_inputs = {"user": {"firstName": first_name,
#                              "lastName": last_name,
#                              "email": email}}

#     response = requests.post(SHEETY_END_POINT, headers=headers, json=sheet_inputs)
#     response.raise_for_status()
#     print(response.text)