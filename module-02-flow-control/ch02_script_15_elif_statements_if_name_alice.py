"""Chapter 2: Flow Control
Section: elif Statements
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter2
Type: book script/example
PPT map: PPT Module-1: boolean, comparison, if/else/elif, while, break/continue, for/range, import, sys.exit
File: ch02_script_15_elif_statements_if_name_alice.py (15 of 37 in this chapter)
"""

   if name == 'Alice':
       print('Hi, Alice.')
   elif age < 12:
       print('You are not Alice, kiddo.')
 elif age > 100:
       print('You are not Alice, grannie.')
   elif age > 2000:
       print('Unlike you, Alice is not an undead, immortal vampire.')
