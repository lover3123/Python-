"""Chapter 15: Keeping Time Scheduling Launching Programs
Section: Step 2: Track and Print Lap Times
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter15
Type: book script/example
PPT map: Syllabus Ch15: time, datetime, subprocess, threading
File: ch15_script_08_step_2_track_and_print_lap_times_python3.py (8 of 37 in this chapter)
"""

   #! python3
   # stopwatch.py - A simple stopwatch program.

   import time

   --snip--

   # Start tracking the lap times.
 try:
    while True:
           input()
         lapTime = round(time.time() - lastTime, 2)
         totalTime = round(time.time() - startTime, 2)
         print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
           lapNum += 1
           lastTime = time.time() # reset the last lap time
 except KeyboardInterrupt:
       # Handle the Ctrl-C exception to keep its error message from displaying.
       print('\nDone.')
