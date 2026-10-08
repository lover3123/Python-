"""Chapter 16: Sending Email and Text Messages
Section: Getting the Body from a Raw Message
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter16
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch16: smtplib, imap, twilio
File: ch16_shell_20_getting_the_body_from_a_raw_message_mess.py (20 of 36 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

message.text_part != None
# OUT:    True
message.text_part.get_payload().decode(message.text_part.charset)
# OUT:  'So long, and thanks for all the fish!\r\n\r\n-Al\r\n'
message.html_part != None
# OUT:    True
message.html_part.get_payload().decode(message.html_part.charset)
# OUT:    '<div dir="ltr"><div>So long, and thanks for all the fish!<br><br></div>-Al
# OUT:    <br></div>\r\n'
