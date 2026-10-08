"""Chapter 16: Sending Email and Text Messages
Section: Retrieving and Deleting Emails with IMAP
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter16
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch16: smtplib, imap, twilio
File: ch16_shell_09_retrieving_and_deleting_emails_with_imap.py (9 of 36 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import imapclient
imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login(' my_email_address@gmail.com ', ' MY_SECRET_PASSWORD ')
# OUT: 'my_email_address@gmail.com Jane Doe authenticated (Success)'
imapObj.select_folder('INBOX', readonly=True)
UIDs = imapObj.search(['SINCE 05-Jul-2014'])
UIDs
# OUT: [40032, 40033, 40034, 40035, 40036, 40037, 40038, 40039, 40040, 40041]
rawMessages = imapObj.fetch([40041], ['BODY[]', 'FLAGS'])
import pyzmail
message = pyzmail.PyzMessage.factory(rawMessages[40041]['BODY[]'])
message.get_subject()
# OUT: 'Hello!'
message.get_addresses('from')
# OUT: [('Edward Snowden', 'esnowden@nsa.gov')]
message.get_addresses('to')
# OUT: [(Jane Doe', 'jdoe@example.com')]
message.get_addresses('cc')
# OUT: []
message.get_addresses('bcc')
# OUT: []
message.text_part != None
# OUT: True
message.text_part.get_payload().decode(message.text_part.charset)
# OUT: 'Follow the money.\r\n\r\n-Ed\r\n'
message.html_part != None
# OUT: True
message.html_part.get_payload().decode(message.html_part.charset)
# OUT: '<div dir="ltr"><div>So long, and thanks for all the fish!<br><br></div>-
# OUT: Al<br></div>\r\n'
imapObj.logout()
