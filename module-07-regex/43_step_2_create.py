# Ch7 | 43/46 | Step 2: Create a Regex for Email Addresses [script]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter7

   #! python3
   # phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.
   import pyperclip, re

   phoneRegex = re.compile(r'''(
   --snip--

   # Create email regex.
   emailRegex = re.compile(r'''(
     [a-zA-Z0-9._%+-]+      # username
     @                      # @ symbol
     [a-zA-Z0-9.-]+         # domain name
       (\.[a-zA-Z]{2,4})      # dot-something
       )''', re.VERBOSE)

   # TODO: Find matches in clipboard text.

   # TODO: Copy results to the clipboard.
