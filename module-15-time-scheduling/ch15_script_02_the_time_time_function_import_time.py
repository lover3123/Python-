"""Chapter 15: Keeping Time Scheduling Launching Programs
Section: The time.time() Function
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter15
Type: book script/example
PPT map: Syllabus Ch15: time, datetime, subprocess, threading
File: ch15_script_02_the_time_time_function_import_time.py (2 of 37 in this chapter)
"""

   import time
 def calcProd():
       # Calculate the product of the first 100,000 numbers.
       product = 1
       for i in range(1, 100000):
           product = product * i
       return product

 startTime = time.time()
   prod = calcProd()
 endTime = time.time()
 print('The result is %s digits long.' % (len(str(prod))))
 print('Took %s seconds to calculate.' % (endTime - startTime))
