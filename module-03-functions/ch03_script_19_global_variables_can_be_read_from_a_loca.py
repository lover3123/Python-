"""Chapter 3: Functions
Section: Global Variables Can Be Read from a Local Scope
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter3
Type: book script/example
PPT map: PPT Unit-2/Module-2: def, params, return, None, keyword args end/sep, local/global scope, recursion, guess-number
File: ch03_script_19_global_variables_can_be_read_from_a_loca.py (19 of 41 in this chapter)
"""

def spam():
    print(eggs)
eggs = 42
spam()
print(eggs)
