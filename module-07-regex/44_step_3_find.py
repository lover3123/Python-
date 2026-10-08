# Ch7 | 44/46 | Step 3: Find All Matches in the Clipboard Text [script]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter7

   #! python3
   # phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

   import pyperclip, re

   phoneRegex = re.compile(r'''(
   --snip--

   # Find matches in clipboard text.
   text = str(pyperclip.paste())
 matches = []
 for groups in phoneRegex.findall(text):
       phoneNum = '-'.join([groups[1], groups[3], groups[5]])
       if groups[8] != '':
           phoneNum += ' x' + groups[8]
       matches.append(phoneNum)
 for groups in emailRegex.findall(text):
       matches.append(groups[0])

   # TODO: Copy results to the clipboard.
