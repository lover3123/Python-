"""Chapter 11: Web Scraping
Section: Getting Data from an Element’s Attributes
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter11
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch11: webbrowser, requests, bs4, selenium
File: ch11_shell_20_getting_data_from_an_element_s_attribute.py (20 of 34 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import bs4
soup = bs4.BeautifulSoup(open('example.html'))
spanElem = soup.select('span')[0]
str(spanElem)
# OUT: '<span id="author">Al Sweigart</span>'
spanElem.get('id')
# OUT: 'author'
spanElem.get('some_nonexistent_addr') == None
# OUT: True
spanElem.attrs
# OUT: {'id': 'author'}
