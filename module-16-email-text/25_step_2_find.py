# Ch16 | 25/36 | Step 2: Find All Unpaid Members [script]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter16

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
