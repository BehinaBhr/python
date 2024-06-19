from twilio.rest import Client

TWILIO_SID = "ACaa0365418ab81d7e959a8e14cce3f9ac"
TWILIO_AUTH_TOKEN = "b256b2f39c056f6b01f9a7abc35b1f4e"
TWILIO_VIRTUAL_NUMBER = '+18509990952'
TWILIO_VERIFIED_NUMBER = '+17788757291'


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
