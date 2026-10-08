# Ch1 | 13/30 | Your First Program [script]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter1

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
