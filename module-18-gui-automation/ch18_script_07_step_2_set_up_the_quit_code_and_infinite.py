"""Chapter 18: GUI Automation Keyboard Mouse
Section: Step 2: Set Up the Quit Code and Infinite Loop
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter18
Type: book script/example
PPT map: Syllabus Ch18: pyautogui
File: ch18_script_07_step_2_set_up_the_quit_code_and_infinite.py (7 of 36 in this chapter)
"""

   #! python3
   # mouseNow.py - Displays the mouse cursor's current position.
   import pyautogui
   print('Press Ctrl-C to quit.')
   try:
       while True:
           # TODO: Get and print the mouse coordinates.
 except KeyboardInterrupt:
     print('\nDone.')
