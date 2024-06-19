# import requests
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# data = response.json()
# print(data)
# longitude = float(response.json()["iss_position"]["longitude"])
# latitude = float(response.json()["iss_position"]["latitude"])
# iss_position = (longitude, latitude)
# print(iss_position)

# TODO: If ISS is close to my position and it is currently dark then send me an email to tell me look up.
# TODO: run the code every 60 seconds.


import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 49.276661
MY_LNG = -122.864243

my_email = "be.bhr77@gmail.com"
password = "dilz ioyp lyjd hkuk"


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_longitude = float(response.json()["iss_position"]["longitude"])
    iss_latitude = float(response.json()["iss_position"]["latitude"])
    # #  Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT - 5 and MY_LNG + 5 <= iss_longitude <= MY_LNG - 5:
        return True


def is_night():
    parameters = {"lat": MY_LAT, "lng": MY_LNG, "formatted": 0}
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    now_hour = datetime.now().hour
    if sunset_hour <= now_hour or now_hour <= sunrise_hour:
        return True

while True:
    time.sleep(60)
    if is_night() and is_iss_overhead():
        with smtplib.SMTP_SSL("smtp.gmail.com", port=465) as connection:
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="appbrewerytesting@yahoo.com",
                                msg="Subject:Look up👆🏻\n\nThe ISS is above you in the sky.")
