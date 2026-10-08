"""Chapter 16: Sending Email and Text Messages
Section: Sending Text Messages
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter16
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch16: smtplib, imap, twilio
File: ch16_shell_31_sending_text_messages_message_status.py (31 of 36 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

message.status
# OUT: 'queued'
message.date_created
# OUT: datetime.datetime(2015, 7, 8, 1, 36, 18)
message.date_sent == None
# OUT: True
