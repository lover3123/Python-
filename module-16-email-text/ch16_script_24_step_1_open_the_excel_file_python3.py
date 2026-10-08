"""Chapter 16: Sending Email and Text Messages
Section: Step 1: Open the Excel File
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter16
Type: book script/example
PPT map: Syllabus Ch16: smtplib, imap, twilio
File: ch16_script_24_step_1_open_the_excel_file_python3.py (24 of 36 in this chapter)
"""

   #! python3
   # sendDuesReminders.py - Sends emails based on payment status in spreadsheet.

   import openpyxl, smtplib, sys

   # Open the spreadsheet and get the latest dues status.
 wb = openpyxl.load_workbook('duesRecords.xlsx')
 sheet = wb.get_sheet_by_name('Sheet1')

 lastCol = sheet.get_highest_column()
 latestMonth = sheet.cell(row=1, column=lastCol).value

   # TODO: Check each member's payment status.

   # TODO: Log in to email account.

   # TODO: Send out reminder emails.
