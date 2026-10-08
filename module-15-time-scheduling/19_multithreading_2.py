# Ch15 | 19/37 | Multithreading [script]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter15

   import threading, time
   print('Start of program.')

 def takeANap():
       time.sleep(5)
       print('Wake up!')

 threadObj = threading.Thread(target=takeANap)
 threadObj.start()

   print('End of program.')
