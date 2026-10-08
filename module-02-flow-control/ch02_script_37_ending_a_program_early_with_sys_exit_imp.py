"""Chapter 2: Flow Control
Section: Ending a Program Early with sys.exit()
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter2
Type: book script/example
PPT map: PPT Module-1: boolean, comparison, if/else/elif, while, break/continue, for/range, import, sys.exit
File: ch02_script_37_ending_a_program_early_with_sys_exit_imp.py (37 of 37 in this chapter)
"""

import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')
