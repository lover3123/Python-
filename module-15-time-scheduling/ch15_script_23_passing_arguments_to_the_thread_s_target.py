"""Chapter 15: Keeping Time Scheduling Launching Programs
Section: Passing Arguments to the Thread’s Target Function
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter15
Type: book script/example
PPT map: Syllabus Ch15: time, datetime, subprocess, threading
File: ch15_script_23_passing_arguments_to_the_thread_s_target.py (23 of 37 in this chapter)
"""

threadObj = threading.Thread(target=print('Cats', 'Dogs', 'Frogs', sep=' & '))
