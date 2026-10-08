"""Chapter 16: Sending Email and Text Messages
Section: Searching for Email
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter16
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch16: smtplib, imap, twilio
File: ch16_shell_14_searching_for_email_uids_imapobj_search_.py (14 of 36 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

UIDs = imapObj.search(['SINCE 05-Jul-2015'])
UIDs
# OUT: [40032, 40033, 40034, 40035, 40036, 40037, 40038, 40039, 40040, 40041]
