import requests
from pprint import pprint

SHEETY_ENDPOINT = "https://api.sheety.co/f3fd64781ef5e3f27c277d9dcf70e696/flightDeals/prices"

# This class is responsible for talking to the Google Sheet.
class DataManager:
    def get_sheet_data(self):
        # TODO: Use Sheety API to make GET requests to print all the data in the sheet.
        response = requests.get(url=SHEETY_ENDPOINT)
        data = response.json()
        # TODO: Try printing the data out again using pprint() to see it formatted.
        # pprint(data)

        # TODO: Pass everything stored in the "prices" key back to the main.py,
        #  store it in a variable called sheet_data, then print the sheet_data from main.py
        sheet_data = data["prices"]
        return sheet_data

    def update_sheet_data(self, row):
        loc = row['id']
        sheet_inputs = {
            'price': {"iataCode": row["iataCode"]}
        }
        response = requests.put(url=f"{SHEETY_ENDPOINT}/{loc}", json=sheet_inputs)
        print(response.text)

    def delete_testing(self, row):
        loc = row['id']
        sheet_inputs = {
            'price': {"iataCode": ""}
        }
        response = requests.put(url=f"{SHEETY_ENDPOINT}/{loc}", json=sheet_inputs)
        print(response.text)





