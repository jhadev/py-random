# import twilio Client
from twilio.rest import Client
import config

client = Client(config.sid, config.token)

receiver = input("Who would you like to text? ex: +15552223333 ")
body = input("Enter your message here: ")
confirm = input("Would you like to send? y/N ")

if confirm == 'y':
    message = client.messages.create(to=receiver,
                                     from_=config.twilio_number,
                                     body=body)
    print("Message sent :)")
else:
    exit()
