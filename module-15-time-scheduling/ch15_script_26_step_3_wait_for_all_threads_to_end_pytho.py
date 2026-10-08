"""Chapter 15: Keeping Time Scheduling Launching Programs
Section: Step 3: Wait for All Threads to End
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter15
Type: book script/example
PPT map: Syllabus Ch15: time, datetime, subprocess, threading
File: ch15_script_26_step_3_wait_for_all_threads_to_end_pytho.py (26 of 37 in this chapter)
"""

#! python3
# multidownloadXkcd.py - Downloads XKCD comics using multiple threads.

--snip--

# Wait for all threads to end.
for downloadThread in downloadThreads:
    downloadThread.join()
print('Done.')
