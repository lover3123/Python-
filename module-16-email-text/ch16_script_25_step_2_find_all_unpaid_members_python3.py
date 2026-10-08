"""Chapter 16: Sending Email and Text Messages
Section: Step 2: Find All Unpaid Members
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter16
Type: book script/example
PPT map: Syllabus Ch16: smtplib, imap, twilio
File: ch16_script_25_step_2_find_all_unpaid_members_python3.py (25 of 36 in this chapter)
"""

   #! python3
   # sendDuesReminders.py - Sends emails based on payment status in spreadsheet.

   --snip--

   # Check each member's payment status.
   unpaidMembers = {}
 for r in range(2, sheet.get_highest_row() + 1):
     payment = sheet.cell(row=r, column=lastCol).value
       if payment != 'paid':
         name = sheet.cell(row=r, column=1).value
         email = sheet.cell(row=r, column=2).value
         unpaidMembers[name] = email
