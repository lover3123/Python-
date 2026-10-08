"""Chapter 10: Debugging
Section: Breakpoints
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter10
Type: book script/example
PPT map: Syllabus Ch10: raise, assert, logging, debugger
File: ch10_script_22_breakpoints_import_random.py (22 of 24 in this chapter)
"""

   import random
   heads = 0
   for i in range(1, 1001):
     if random.randint(0, 1) == 1:
           heads = heads + 1
       if i == 500:
         print('Halfway done!')
   print('Heads came up ' + str(heads) + ' times.')
