# Ch10 | 18/24 | Disabling Logging [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter10

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
