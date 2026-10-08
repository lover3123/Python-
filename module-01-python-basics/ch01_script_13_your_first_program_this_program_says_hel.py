"""Chapter 1: Python Basics
Section: Your First Program
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter1
Type: book script/example
PPT map: PPT Module-1: intro, expressions, datatypes, variables, print/input/len/str-int-float, operators
File: ch01_script_13_your_first_program_this_program_says_hel.py (13 of 30 in this chapter)
"""

 # This program says hello and asks for my name.

 print('Hello world!')
   print('What is your name?')    # ask for their name
 myName = input()
 print('It is good to meet you, ' + myName)
 print('The length of your name is:')
   print(len(myName))
 print('What is your age?')    # ask for their age
   myAge = input()
   print('You will be ' + str(int(myAge) + 1) + ' in a year.')
