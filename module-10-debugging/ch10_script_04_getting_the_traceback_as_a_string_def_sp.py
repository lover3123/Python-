"""Chapter 10: Debugging
Section: Getting the Traceback as a String
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter10
Type: book script/example
PPT map: Syllabus Ch10: raise, assert, logging, debugger
File: ch10_script_04_getting_the_traceback_as_a_string_def_sp.py (4 of 24 in this chapter)
"""

def spam():
    bacon()
def bacon():
    raise Exception('This is the error message.')

spam()
