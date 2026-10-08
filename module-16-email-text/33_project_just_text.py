# Ch16 | 33/36 | Project: “Just Text Me” Module [script]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter16

   #! python3
   # textMyself.py - Defines the textmyself() function that texts a message
   # passed to it as a string.

   # Preset values:
   accountSID = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
   authToken = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
   myNumber = '+15559998888'
   twilioNumber = '+15552225678'

   from twilio.rest import TwilioRestClient

 def textmyself(message):
     twilioCli = TwilioRestClient(accountSID, authToken)
     twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)
