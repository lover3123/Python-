"""Chapter 18: GUI Automation Keyboard Mouse
Section: Dragging the Mouse
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter18
Type: book script/example
PPT map: Syllabus Ch18: pyautogui
File: ch18_script_12_dragging_the_mouse_import_pyautogui_time.py (12 of 36 in this chapter)
"""

   import pyautogui, time
 time.sleep(5)
 pyautogui.click()    # click to put drawing program in focus
   distance = 200
   while distance > 0:
     pyautogui.dragRel(distance, 0, duration=0.2)   # move right
     distance = distance - 5
     pyautogui.dragRel(0, distance, duration=0.2)   # move down
     pyautogui.dragRel(-distance, 0, duration=0.2)  # move left
       distance = distance - 5
       pyautogui.dragRel(0, -distance, duration=0.2)  # move up
