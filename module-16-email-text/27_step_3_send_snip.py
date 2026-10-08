# Ch16 | 27/36 | Step 3: Send Customized Email Reminders [script]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter16

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
