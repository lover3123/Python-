"""Chapter 3: Functions
Section: Local Variables Cannot Be Used in the Global Scope
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter3
Type: book script/example
PPT map: PPT Unit-2/Module-2: def, params, return, None, keyword args end/sep, local/global scope, recursion, guess-number
File: ch03_script_16_local_variables_cannot_be_used_in_the_gl.py (16 of 41 in this chapter)
"""

def spam():
    eggs = 31337
spam()
print(eggs)
