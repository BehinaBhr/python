# TODO: if any of the flights found are cheaper than the Lowest Price listed in the Google Sheet.
#  by using Twilio API send an SMS to book the flight in NotificationManager class
#  The message should include: Price, Departure City Name, Departure Airport IATA Code,
#  Arrival City Name, Arrival Airport IATA Code, Outbound Date ,Inbound Date


# This class is responsible for sending notifications with the deal flight details.

from twilio.rest import Client

class NotificationManager:
    def send_sms(self,message):
        account_sid = "ACaa0365418ab81d7e959a8e14cce3f9ac"
        auth_token = "b256b2f39c056f6b01f9a7abc35b1f4e"
        client = Client(account_sid, auth_token)
        message = client.messages.create(from_='+18509990952', body=message, to='+17788757291')
        print(message.status)
        # # Prints if successfully sent.
        # print(message.sid)