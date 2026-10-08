"""Chapter 16: Sending Email and Text Messages
Section: Step 3: Send Customized Email Reminders
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter16
Type: book script/example
PPT map: Syllabus Ch16: smtplib, imap, twilio
File: ch16_script_27_step_3_send_customized_email_reminders_p.py (27 of 36 in this chapter)
"""

   #! python3
   # sendDuesReminders.py - Sends emails based on payment status in spreadsheet.

   --snip--

   # Send out reminder emails.
   for name, email in unpaidMembers.items():
     body = "Subject: %s dues unpaid.\nDear %s,\nRecords show that you have not
   paid dues for %s. Please make this payment as soon as possible. Thank you!'" %
   (latestMonth, name, latestMonth)
     print('Sending email to %s...' % email)
     sendmailStatus = smtpObj.sendmail('my_email_address@gmail.com', email, body)

     if sendmailStatus != {}:
           print('There was a problem sending email to %s: %s' % (email,
           sendmailStatus))
   smtpObj.quit()
