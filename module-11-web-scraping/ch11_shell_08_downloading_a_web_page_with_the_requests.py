"""Chapter 11: Web Scraping
Section: Downloading a Web Page with the requests.get() Function
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter11
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch11: webbrowser, requests, bs4, selenium
File: ch11_shell_08_downloading_a_web_page_with_the_requests.py (8 of 34 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
type(res)
# OUT:    <class 'requests.models.Response'>
res.status_code == requests.codes.ok
# OUT:    True
len(res.text)
# OUT:    178981
print(res.text[:250])
# OUT:    The Project Gutenberg EBook of Romeo and Juliet, by William Shakespeare

# OUT:    This eBook is for the use of anyone anywhere at no cost and with
# OUT:    almost no restrictions whatsoever. You may copy it, give it away or
# OUT:    re-use it under the terms of the Proje
