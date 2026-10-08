"""Chapter 3: Functions
Section: Local Scopes Cannot Use Variables in Other Local Scopes
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter3
Type: book script/example
PPT map: PPT Unit-2/Module-2: def, params, return, None, keyword args end/sep, local/global scope, recursion, guess-number
File: ch03_script_18_local_scopes_cannot_use_variables_in_oth.py (18 of 41 in this chapter)
"""

  def spam():
    eggs = 99
    bacon()
    print(eggs)

  def bacon():
      ham = 101
    eggs = 0

 spam()
