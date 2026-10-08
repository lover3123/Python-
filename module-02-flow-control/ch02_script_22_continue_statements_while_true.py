"""Chapter 2: Flow Control
Section: continue Statements
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter2
Type: book script/example
PPT map: PPT Module-1: boolean, comparison, if/else/elif, while, break/continue, for/range, import, sys.exit
File: ch02_script_22_continue_statements_while_true.py (22 of 37 in this chapter)
"""

  while True:
      print('Who are you?')
      name = input()
    if name != 'Joe':
        continue
      print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
      if password == 'swordfish':
        break
 print('Access granted.')
