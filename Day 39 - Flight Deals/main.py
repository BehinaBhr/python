# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.

# TODO: Pass everything stored in the "prices" key back to the main.py,
#  store it in a variable called sheet_data, then print the sheet_data from main.py
from data_manager import DataManager

data_manager = DataManager()
sheet_data = data_manager.get_sheet_data()
# print(sheet_data)


# TODO: In main.py check if sheet_data contains any values for the "iataCode" key.
#  If not, then the IATA Codes column is empty in the Google Sheet.
#  In this case, pass each city name in sheet_data one-by-one to the FlightSearch class.
#  For now, the FlightSearch class can respond with "TESTING" instead of a real IATA code.
# TODO: for real IATA codes: Pass each city name in sheet_data one-by-one to the FlightSearch class
#  to get the corresponding IATA code for that city. then update the sheet_data.

for row in sheet_data:
    # print(row)
    # print(row['iataCode'])
    if row['iataCode'] == "":
        from flight_search import FlightSearch
        flight_search = FlightSearch()
        flight_search.get_iata_code(row)
    # print(f"new_sheet_data:\n {sheet_data}")
# TODO: use the IATA code response from the FlightSearch class to
#  update the sheet_data in DataManager Class by making a PUT request,
#  use the row id from sheet_data to update the Google Sheet with the IATA codes then Print the updated sheet_data.
        data_manager.update_sheet_data(row)

# TODO: Delete the "TESTING" values in the Google sheet again

    # elif row['iataCode'] == "TESTING":
    #     data_manager.delete_testing(row)

print(sheet_data)

# TODO: search for the flight prices from London (LON) to all the cities.
#  only for direct flights, that leave anytime between tomorrow and
#  in 6 months (6x30days) time with timedelta() from the datatime module to define a 6 month period.
#  round trips that return between 7 and 28 days in length.
#  use strftime() to format the date to the required format by the Flight Search API.
#  use split() to get the first part of the date from the API response.

from datetime import datetime, timedelta
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))


for travel in sheet_data:
    destination_code = travel['iataCode']
    travel_city_name = travel['city']
    from flight_data import FlightData
    flight_data = FlightData()
    travel_price, travel_out_date, travel_return_date = flight_data.check_flights(destination_code, from_time=tomorrow, to_time=six_month_from_today)
    if travel_price < travel["lowestPrice"]:
        from notification_manager import NotificationManager
        notification_manager = NotificationManager()
        notification_manager.send_sms(message=f"Low price alert! Only £{travel_price} to fly from London-LON to {travel_city_name}-{destination_code}"
                                              f" between {travel_out_date} to {travel_return_date}.")
