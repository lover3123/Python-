"""Chapter 18: GUI Automation Keyboard Mouse
Section: Step 3: Start Typing Data
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter18
Type: book script/example
PPT map: Syllabus Ch18: pyautogui
File: ch18_script_34_step_3_start_typing_data_python3.py (34 of 36 in this chapter)
"""

   #! python3
   # formFiller.py - Automatically fills in the form.

   --snip--

     print('Entering %s info...' % (person['name']))
     pyautogui.click(nameField[0], nameField[1])

       # Fill out the Name field.
     pyautogui.typewrite(person['name'] + '\t')

       # Fill out the Greatest Fear(s) field.
     pyautogui.typewrite(person['fear'] + '\t')

   --snip--
