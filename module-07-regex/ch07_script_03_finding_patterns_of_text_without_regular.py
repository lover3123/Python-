"""Chapter 7: Pattern Matching with Regular Expressions
Section: Finding Patterns of Text Without Regular Expressions
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter7
Type: book script/example
PPT map: Syllabus Ch7: regex
File: ch07_script_03_finding_patterns_of_text_without_regular.py (3 of 46 in this chapter)
"""

   message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
   for i in range(len(message)):
     chunk = message[i:i+12]
     if isPhoneNumber(chunk):
         print('Phone number found: ' + chunk)
   print('Done')
