"""Chapter 16: Sending Email and Text Messages
Section: Sending Text Messages
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter16
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch16: smtplib, imap, twilio
File: ch16_shell_29_sending_text_messages_from_twilio_rest_i.py (29 of 36 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

from twilio.rest import TwilioRestClient
accountSID = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
authToken = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
twilioCli = TwilioRestClient(accountSID, authToken)
myTwilioNumber = '+14955551234'
myCellPhone = '+14955558888'
message = twilioCli.messages.create(body='Mr. Watson - Come here - I want
# OUT:    to see you.', from_=myTwilioNumber, to=myCellPhone)
