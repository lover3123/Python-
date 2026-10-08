# Ch18 | 34/36 | Step 3: Start Typing Data [script]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter18

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
