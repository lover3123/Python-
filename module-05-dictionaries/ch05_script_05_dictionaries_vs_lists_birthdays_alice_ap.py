"""Chapter 5: Dictionaries and Structuring Data
Section: Dictionaries vs. Lists
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter5
Type: book script/example
PPT map: Syllabus Ch5: dicts, structuring data
File: ch05_script_05_dictionaries_vs_lists_birthdays_alice_ap.py (5 of 37 in this chapter)
"""

 birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

   while True:
       print('Enter a name: (blank to quit)')
       name = input()
       if name == '':
           break

     if name in birthdays:
         print(birthdays[name] + ' is the birthday of ' + name)
       else:
           print('I do not have birthday information for ' + name)
           print('What is their birthday?')
           bday = input()
         birthdays[name] = bday
           print('Birthday database updated.')
