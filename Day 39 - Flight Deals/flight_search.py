import requests

TEQUILA_LOCATION_API_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
TEQUILA_API_KEY = "p0J8osvKNfDi7bzAEd3arP0V1oJwqZLP"

# This class is responsible for talking to the Flight Search API.
class FlightSearch:
    def get_iata_code(self, row):
        # Return "TESTING" for now to make sure Sheety is working. Get TEQUILA API data later.
        city_name = row['city']
        # row['iataCode'] = "TESTING"
        # return row['iataCode']

        # Return the missing IATA codes for each city by making get requests from the Kiwi Partners Tequila API (search by query)
        parameters = {"term": city_name, "location_types": "city"}
        headers = {"apikey": TEQUILA_API_KEY}
        response = requests.get(TEQUILA_LOCATION_API_ENDPOINT, params=parameters, headers=headers)
        results = response.json()
        # print(results)
        row['iataCode'] = results["locations"][0]["code"]
        return row['iataCode']







