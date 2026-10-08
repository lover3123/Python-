"""Chapter 10: Debugging
Section: Using the logging Module
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter10
Type: book script/example
PPT map: Syllabus Ch10: raise, assert, logging, debugger
File: ch10_script_13_using_the_logging_module_import_logging.py (13 of 24 in this chapter)
"""

import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s
- %(message)s')
