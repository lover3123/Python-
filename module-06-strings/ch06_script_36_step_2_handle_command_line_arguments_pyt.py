"""Chapter 6: Manipulating Strings
Section: Step 2: Handle Command Line Arguments
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter6
Type: book script/example
PPT map: Syllabus Ch6: strings, text editing
File: ch06_script_36_step_2_handle_command_line_arguments_pyt.py (36 of 46 in this chapter)
"""

#! python3
# pw.py - An insecure password locker program.

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

import sys
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]      # first command line arg is the account name
