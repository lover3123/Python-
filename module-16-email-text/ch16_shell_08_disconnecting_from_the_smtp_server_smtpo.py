"""Chapter 16: Sending Email and Text Messages
Section: Disconnecting from the SMTP Server
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter16
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch16: smtplib, imap, twilio
File: ch16_shell_08_disconnecting_from_the_smtp_server_smtpo.py (8 of 36 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

smtpObj.quit()
# OUT: (221, b'2.0.0 closing connection ko10sm23097611pbd.52 - gsmtp')
