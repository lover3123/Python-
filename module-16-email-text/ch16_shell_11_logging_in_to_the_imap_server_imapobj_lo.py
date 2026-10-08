"""Chapter 16: Sending Email and Text Messages
Section: Logging in to the IMAP Server
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter16
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch16: smtplib, imap, twilio
File: ch16_shell_11_logging_in_to_the_imap_server_imapobj_lo.py (11 of 36 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

imapObj.login(' my_email_address@gmail.com ', ' MY_SECRET_PASSWORD ')
# OUT: 'my_email_address@gmail.com Jane Doe authenticated (Success)'
