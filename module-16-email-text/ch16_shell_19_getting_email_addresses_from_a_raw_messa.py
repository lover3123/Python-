"""Chapter 16: Sending Email and Text Messages
Section: Getting Email Addresses from a Raw Message
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter16
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch16: smtplib, imap, twilio
File: ch16_shell_19_getting_email_addresses_from_a_raw_messa.py (19 of 36 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

message.get_subject()
# OUT: 'Hello!'
message.get_addresses('from')
# OUT: [('Edward Snowden', 'esnowden@nsa.gov')]
message.get_addresses('to')
# OUT: [(Jane Doe', 'my_email_address@gmail.com')]
message.get_addresses('cc')
# OUT: []
message.get_addresses('bcc')
# OUT: []
