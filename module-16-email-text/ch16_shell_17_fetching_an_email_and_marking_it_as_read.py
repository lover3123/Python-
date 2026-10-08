"""Chapter 16: Sending Email and Text Messages
Section: Fetching an Email and Marking It As Read
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter16
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch16: smtplib, imap, twilio
File: ch16_shell_17_fetching_an_email_and_marking_it_as_read.py (17 of 36 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

imapObj.select_folder('INBOX', readonly=False)
