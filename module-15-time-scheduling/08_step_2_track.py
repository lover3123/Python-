# Ch15 | 08/37 | Step 2: Track and Print Lap Times [script]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter15

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
