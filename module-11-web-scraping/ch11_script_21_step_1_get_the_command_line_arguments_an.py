"""Chapter 11: Web Scraping
Section: Step 1: Get the Command Line Arguments and Request the Search Page
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter11
Type: book script/example
PPT map: Syllabus Ch11: webbrowser, requests, bs4, selenium
File: ch11_script_21_step_1_get_the_command_line_arguments_an.py (21 of 34 in this chapter)
"""

#! python3
# lucky.py - Opens several Google search results.

import requests, sys, webbrowser, bs4

print('Googling...') # display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# TODO: Retrieve top search result links.

# TODO: Open a browser tab for each result.
