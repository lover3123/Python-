"""Chapter 7: Pattern Matching with Regular Expressions
Section: Step 2: Create a Regex for Email Addresses
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter7
Type: book script/example
PPT map: Syllabus Ch7: regex
File: ch07_script_43_step_2_create_a_regex_for_email_addresse.py (43 of 46 in this chapter)
"""

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
