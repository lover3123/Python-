"""Chapter 16: Sending Email and Text Messages
Section: Sending the SMTP “Hello” Message
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter16
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch16: smtplib, imap, twilio
File: ch16_shell_04_sending_the_smtp_hello_message_smtpobj_e.py (4 of 36 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

smtpObj.ehlo()
# OUT: (250, b'mx.google.com at your service, [216.172.148.131]\nSIZE 35882577\
# OUT: n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nCHUNKING')
