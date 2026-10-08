"""Chapter 7: Pattern Matching with Regular Expressions
Section: Finding Patterns of Text Without Regular Expressions
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter7
Type: book script/example
PPT map: Syllabus Ch7: regex
File: ch07_script_01_finding_patterns_of_text_without_regular.py (1 of 46 in this chapter)
"""

   def isPhoneNumber(text):
     if len(text) != 12:
           return False
       for i in range(0, 3):
         if not text[i].isdecimal():
               return False
     if text[3] != '-':
           return False
       for i in range(4, 7):
         if not text[i].isdecimal():
               return False
     if text[7] != '-':
           return False
       for i in range(8, 12):
         if not text[i].isdecimal():
               return False
     return True

   print('415-555-4242 is a phone number:')
   print(isPhoneNumber('415-555-4242'))
   print('Moshi moshi is a phone number:')
   print(isPhoneNumber('Moshi moshi'))
