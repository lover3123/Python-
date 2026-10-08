"""Chapter 16: Sending Email and Text Messages
Section: Sending an Email
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter16
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch16: smtplib, imap, twilio
File: ch16_shell_07_sending_an_email_smtpobj_sendmail_my_ema.py (7 of 36 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

smtpObj.sendmail(' my_email_address@gmail.com ', ' recipient@example.com ',
# OUT: 'Subject: So long.\nDear Alice, so long and thanks for all the fish. Sincerely,
# OUT: Bob')
# OUT: {}
