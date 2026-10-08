"""Chapter 10: Debugging
Section: Disabling Logging
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter10
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch10: raise, assert, logging, debugger
File: ch10_shell_18_disabling_logging_import_logging.py (18 of 24 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import logging
logging.basicConfig(level=logging.INFO, format=' %(asctime)s -
# OUT: %(levelname)s - %(message)s')
logging.critical('Critical error! Critical error!')
# OUT: 2015-05-22 11:10:48,054 - CRITICAL - Critical error! Critical error!
logging.disable(logging.CRITICAL)
logging.critical('Critical error! Critical error!')
logging.error('Error! Error!')
