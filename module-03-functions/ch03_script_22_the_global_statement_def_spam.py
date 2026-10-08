"""Chapter 3: Functions
Section: The global Statement
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter3
Type: book script/example
PPT map: PPT Unit-2/Module-2: def, params, return, None, keyword args end/sep, local/global scope, recursion, guess-number
File: ch03_script_22_the_global_statement_def_spam.py (22 of 41 in this chapter)
"""

  def spam():
    global eggs
    eggs = 'spam'

  eggs = 'global'
  spam()
  print(eggs)
