"""Chapter 11: Web Scraping
Section: Saving Downloaded Files to the Hard Drive
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter11
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch11: webbrowser, requests, bs4, selenium
File: ch11_shell_12_saving_downloaded_files_to_the_hard_driv.py (12 of 34 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
# OUT:         playFile.write(chunk)

# OUT: 100000
# OUT: 78981
playFile.close()
