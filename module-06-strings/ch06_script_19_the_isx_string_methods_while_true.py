"""Chapter 6: Manipulating Strings
Section: The isX String Methods
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter6
Type: book script/example
PPT map: Syllabus Ch6: strings, text editing
File: ch06_script_19_the_isx_string_methods_while_true.py (19 of 46 in this chapter)
"""

while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')

while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers.')
