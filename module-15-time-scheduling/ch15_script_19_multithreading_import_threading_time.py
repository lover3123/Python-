"""Chapter 15: Keeping Time Scheduling Launching Programs
Section: Multithreading
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter15
Type: book script/example
PPT map: Syllabus Ch15: time, datetime, subprocess, threading
File: ch15_script_19_multithreading_import_threading_time.py (19 of 37 in this chapter)
"""

   import threading, time
   print('Start of program.')

 def takeANap():
       time.sleep(5)
       print('Wake up!')

 threadObj = threading.Thread(target=takeANap)
 threadObj.start()

   print('End of program.')
