# Ch18 | 07/36 | Step 2: Set Up the Quit Code and Infinite Loop [script]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter18

   #! python3
   # mouseNow.py - Displays the mouse cursor's current position.
   import pyautogui
   print('Press Ctrl-C to quit.')
   try:
       while True:
           # TODO: Get and print the mouse coordinates.
 except KeyboardInterrupt:
     print('\nDone.')
