"""Chapter 16: Sending Email and Text Messages
Section: Searching for Email
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter16
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch16: smtplib, imap, twilio
File: ch16_shell_12_searching_for_email_import_pprint.py (12 of 36 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import pprint
pprint.pprint(imapObj.list_folders())
# OUT: [(('\\HasNoChildren',), '/', 'Drafts'),
# OUT:  (('\\HasNoChildren',), '/', 'Filler'),
# OUT:  (('\\HasNoChildren',), '/', 'INBOX'),
# OUT:  (('\\HasNoChildren',), '/', 'Sent'),
# OUT: --snip-
# OUT:  (('\\HasNoChildren', '\\Flagged'), '/', '[Gmail]/Starred'),
# OUT:  (('\\HasNoChildren', '\\Trash'), '/', '[Gmail]/Trash')]
