"""Chapter 16: Sending Email and Text Messages
Section: Sending Email
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter16
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch16: smtplib, imap, twilio
File: ch16_shell_01_sending_email_import_smtplib.py (1 of 36 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import smtplib
smtpObj = smtplib.SMTP('smtp.example.com', 587)
smtpObj.ehlo()
# OUT: (250, b'mx.example.com at your service, [216.172.148.131]\nSIZE 35882577\
# OUT: n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nCHUNKING')
smtpObj.starttls()
# OUT: (220, b'2.0.0 Ready to start TLS')
smtpObj.login('bob@example.com', ' MY_SECRET_PASSWORD')
# OUT: (235, b'2.7.0 Accepted')
smtpObj.sendmail('bob@example.com', 'alice@example.com', 'Subject: So
# OUT: long.\nDear Alice, so long and thanks for all the fish. Sincerely, Bob')
# OUT: {}
smtpObj.quit()
# OUT: (221, b'2.0.0 closing connection ko10sm23097611pbd.52 - gsmtp')
