"""Chapter 3: Functions
Section: Return Values and return Statements
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter3
Type: book script/example
PPT map: PPT Unit-2/Module-2: def, params, return, None, keyword args end/sep, local/global scope, recursion, guess-number
File: ch03_script_07_return_values_and_return_statements_r_ra.py (7 of 41 in this chapter)
"""

r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)
