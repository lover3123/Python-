# Ch15 | 34/37 | Step 1: Count Down [script]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter15

   #! python3
   # countdown.py - A simple countdown script.

   import time, subprocess

 timeLeft = 60
   while timeLeft > 0:
     print(timeLeft, end='')
     time.sleep(1)
     timeLeft = timeLeft - 1

   # TODO: At the end of the countdown, play a sound file.
