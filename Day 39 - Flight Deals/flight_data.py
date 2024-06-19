# This class is responsible for structuring the flight data.
# TODO: use Flight Search API to make GET requests to print print the City and Price for all the cities

# TODO: search for the flight prices from London (LON) to all the cities.
#  only for direct flights, that leave anytime between tomorrow and
#  in 6 months (6x30days) time with timedelta() from the datatime module to define a 6 month period.
#  round trips that return between 7 and 28 days in length.
#  use strftime() to format the date to the required format by the Flight Search API.
#  use split() to get the first part of the date from the API response.
#  The currency of the price should be in GBP.
#  create attributes for price, departure_airport_code, departure_city etc.

import requests

TEQUILA_API_KEY = "p0J8osvKNfDi7bzAEd3arP0V1oJwqZLP"
TEQUILA_SEARCH_API_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"


class FlightData:

    def check_flights(self, destination_code, from_time, to_time):
        headers = {"apikey": TEQUILA_API_KEY}
        parameters = {"fly_from": "LON", "fly_to": destination_code,
                      "date_from": from_time.strftime("%d/%m/%Y"),
                      "date_to": to_time.strftime("%d/%m/%Y"),
                      "nights_in_dst_from": 7,
                      "nights_in_dst_to": 28,
                      "flight_type": "round",
                      "one_for_city": 1,
                      "max_stopovers": 0,
                      "curr": "GBP"}
        response = requests.get(TEQUILA_SEARCH_API_ENDPOINT, params=parameters, headers=headers)
        results = response.json()["data"][0]
        # print(results)
        print(f"{results["cityTo"]}: £{results["price"]}")

        price = results["price"]
        # origin_city = results["route"][0]["cityFrom"]
        # origin_airport = results["route"][0]["flyFrom"]
        # destination_city = results["route"][0]["cityTo"]
        # destination_airport = results["route"][0]["flyTo"]
        out_date = results["route"][0]["local_departure"].split("T")[0]
        return_date = results["route"][1]["local_departure"].split("T")[0]
        return price, out_date, return_date

        # try:
        #     results = response.json()["data"][0]
        # except IndexError:
        #     print(f"No flights found for {destination_code}.")
        #     return None
