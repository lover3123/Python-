"""Chapter 16: Sending Email and Text Messages
Section: Project: “Just Text Me” Module
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter16
Type: book script/example
PPT map: Syllabus Ch16: smtplib, imap, twilio
File: ch16_script_33_project_just_text_me_module_python3.py (33 of 36 in this chapter)
"""

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
