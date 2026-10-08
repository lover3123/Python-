"""Chapter 18: GUI Automation Keyboard Mouse
Section: Step 4: Handle Select Lists and Radio Buttons
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter18
Type: book script/example
PPT map: Syllabus Ch18: pyautogui
File: ch18_script_35_step_4_handle_select_lists_and_radio_but.py (35 of 36 in this chapter)
"""

   #! python3
   # formFiller.py - Automatically fills in the form.

   --snip--

       # Fill out the Source of Wizard Powers field.
     if person['source'] == 'wand':
         pyautogui.typewrite(['down', '\t'])
       elif person['source'] == 'amulet':
           pyautogui.typewrite(['down', 'down', '\t'])
       elif person['source'] == 'crystal ball':
           pyautogui.typewrite(['down', 'down', 'down', '\t'])
       elif person['source'] == 'money':
           pyautogui.typewrite(['down', 'down', 'down', 'down', '\t'])

       # Fill out the Robocop field.
     if person['robocop'] == 1:
         pyautogui.typewrite([' ', '\t'])
       elif person['robocop'] == 2:
           pyautogui.typewrite(['right', '\t'])
       elif person['robocop'] == 3:
           pyautogui.typewrite(['right', 'right', '\t'])
       elif person['robocop'] == 4:
           pyautogui.typewrite(['right', 'right', 'right', '\t'])
       elif person['robocop'] == 5:
           pyautogui.typewrite(['right', 'right', 'right', 'right', '\t'])

   --snip--
