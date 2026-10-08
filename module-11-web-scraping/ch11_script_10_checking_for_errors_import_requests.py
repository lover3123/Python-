"""Chapter 11: Web Scraping
Section: Checking for Errors
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter11
Type: book script/example
PPT map: Syllabus Ch11: webbrowser, requests, bs4, selenium
File: ch11_script_10_checking_for_errors_import_requests.py (10 of 34 in this chapter)
"""

import requests
res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))
