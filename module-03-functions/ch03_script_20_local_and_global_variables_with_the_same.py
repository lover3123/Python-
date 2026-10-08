"""Chapter 3: Functions
Section: Local and Global Variables with the Same Name
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter3
Type: book script/example
PPT map: PPT Unit-2/Module-2: def, params, return, None, keyword args end/sep, local/global scope, recursion, guess-number
File: ch03_script_20_local_and_global_variables_with_the_same.py (20 of 41 in this chapter)
"""

   def spam():
     eggs = 'spam local'
       print(eggs) # prints 'spam local'
   def bacon():

     eggs = 'bacon local'
       print(eggs) # prints 'bacon local'
       spam()
       print(eggs) # prints 'bacon local'

 eggs = 'global'
   bacon()
   print(eggs) # prints 'global'
