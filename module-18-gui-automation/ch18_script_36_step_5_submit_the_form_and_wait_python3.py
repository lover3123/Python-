"""Chapter 18: GUI Automation Keyboard Mouse
Section: Step 5: Submit the Form and Wait
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter18
Type: book script/example
PPT map: Syllabus Ch18: pyautogui
File: ch18_script_36_step_5_submit_the_form_and_wait_python3.py (36 of 36 in this chapter)
"""

#! python3
# formFiller.py - Automatically fills in the form.

--snip--

    # Fill out the Additional Comments field.
    pyautogui.typewrite(person['comments'] + '\t')

    # Click Submit.
    pyautogui.press('enter')

    # Wait until form page has loaded.
    print('Clicked Submit.')
    time.sleep(5)

    # Click the Submit another response link.
    pyautogui.click(submitAnotherLink[0], submitAnotherLink[1])
