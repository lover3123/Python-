"""Chapter 2: Flow Control
Section: break Statements
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter2
Type: book script/example
PPT map: PPT Module-1: boolean, comparison, if/else/elif, while, break/continue, for/range, import, sys.exit
File: ch02_script_21_break_statements_while_true.py (21 of 37 in this chapter)
"""

 while True:
       print('Please type your name.')
     name = input()
     if name == 'your name':
         break
 print('Thank you!')
