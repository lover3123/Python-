"""Chapter 16: Sending Email and Text Messages
Section: Step 3: Send Customized Email Reminders
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter16
Type: book script/example
PPT map: Syllabus Ch16: smtplib, imap, twilio
File: ch16_script_26_step_3_send_customized_email_reminders_p.py (26 of 36 in this chapter)
"""

#! python3
# sendDuesReminders.py - Sends emails based on payment status in spreadsheet.

--snip--

# Log in to email account.
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(' my_email_address@gmail.com ', sys.argv[1])
