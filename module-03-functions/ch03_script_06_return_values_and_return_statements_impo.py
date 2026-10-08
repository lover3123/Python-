"""Chapter 3: Functions
Section: Return Values and return Statements
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter3
Type: book script/example
PPT map: PPT Unit-2/Module-2: def, params, return, None, keyword args end/sep, local/global scope, recursion, guess-number
File: ch03_script_06_return_values_and_return_statements_impo.py (6 of 41 in this chapter)
"""

 import random
 def getAnswer(answerNumber):
     if answerNumber == 1:
           return 'It is certain'
       elif answerNumber == 2:
           return 'It is decidedly so'
       elif answerNumber == 3:
           return 'Yes'
       elif answerNumber == 4:
           return 'Reply hazy try again'
       elif answerNumber == 5:
           return 'Ask again later'
       elif answerNumber == 6:
           return 'Concentrate and ask again'
       elif answerNumber == 7:
           return 'My reply is no'
       elif answerNumber == 8:
           return 'Outlook not so good'
       elif answerNumber == 9:
           return 'Very doubtful'

 r = random.randint(1, 9)
 fortune = getAnswer(r)
 print(fortune)
