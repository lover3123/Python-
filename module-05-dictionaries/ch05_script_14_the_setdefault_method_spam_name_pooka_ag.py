"""Chapter 5: Dictionaries and Structuring Data
Section: The setdefault() Method
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter5
Type: book script/example
PPT map: Syllabus Ch5: dicts, structuring data
File: ch05_script_14_the_setdefault_method_spam_name_pooka_ag.py (14 of 37 in this chapter)
"""

spam = {'name': 'Pooka', 'age': 5}
if 'color' not in spam:
    spam['color'] = 'black'
