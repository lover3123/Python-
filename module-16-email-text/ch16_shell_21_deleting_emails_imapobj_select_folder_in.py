"""Chapter 16: Sending Email and Text Messages
Section: Deleting Emails
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter16
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch16: smtplib, imap, twilio
File: ch16_shell_21_deleting_emails_imapobj_select_folder_in.py (21 of 36 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

imapObj.select_folder('INBOX', readonly=False)
UIDs = imapObj.search(['ON 09-Jul-2015'])
UIDs
# OUT:    [40066]
imapObj.delete_messages(UIDs)
# OUT:  {40066: ('\\Seen', '\\Deleted')}
imapObj.expunge()
# OUT:    ('Success', [(5452, 'EXISTS')])
