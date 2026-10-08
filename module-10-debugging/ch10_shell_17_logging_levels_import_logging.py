"""Chapter 10: Debugging
Section: Logging Levels
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter10
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch10: raise, assert, logging, debugger
File: ch10_shell_17_logging_levels_import_logging.py (17 of 24 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -
# OUT: %(levelname)s - %(message)s')
logging.debug('Some debugging details.')
# OUT: 2015-05-18 19:04:26,901 - DEBUG - Some debugging details.
logging.info('The logging module is working.')
# OUT: 2015-05-18 19:04:35,569 - INFO - The logging module is working.
logging.warning('An error message is about to be logged.')
# OUT: 2015-05-18 19:04:56,843 - WARNING - An error message is about to be logged.
logging.error('An error has occurred.')
# OUT: 2015-05-18 19:05:07,737 - ERROR - An error has occurred.
logging.critical('The program is unable to recover!')
# OUT: 2015-05-18 19:05:45,794 - CRITICAL - The program is unable to recover!
