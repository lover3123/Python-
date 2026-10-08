"""Chapter 18: GUI Automation Keyboard Mouse
Section: Step 3: Get and Print the Mouse Coordinates
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter18
Type: book script/example
PPT map: Syllabus Ch18: pyautogui
File: ch18_script_09_step_3_get_and_print_the_mouse_coordinat.py (9 of 36 in this chapter)
"""

   #! python3
   # mouseNow.py - Displays the mouse cursor's current position.
   --snip--
           print(positionStr, end='')
         print('\b' * len(positionStr), end='', flush=True)
