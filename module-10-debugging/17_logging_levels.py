# Ch10 | 17/24 | Logging Levels [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter10

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
