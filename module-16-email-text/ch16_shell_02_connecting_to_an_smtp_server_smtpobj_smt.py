"""Chapter 16: Sending Email and Text Messages
Section: Connecting to an SMTP Server
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter16
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch16: smtplib, imap, twilio
File: ch16_shell_02_connecting_to_an_smtp_server_smtpobj_smt.py (2 of 36 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
type(smtpObj)
# OUT: <class 'smtplib.SMTP'>
