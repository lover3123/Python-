"""Chapter 15: Keeping Time Scheduling Launching Programs
Section: Pausing Until a Specific Date
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter15
Type: book script/example
PPT map: Syllabus Ch15: time, datetime, subprocess, threading
File: ch15_script_15_pausing_until_a_specific_date_import_dat.py (15 of 37 in this chapter)
"""

import datetime
import time
halloween2016 = datetime.datetime(2016, 10, 31, 0, 0, 0)
while datetime.datetime.now() < halloween2016:
    time.sleep(1)
