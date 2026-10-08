"""Chapter 11: Web Scraping
Section: Creating a BeautifulSoup Object from HTML
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter11
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch11: webbrowser, requests, bs4, selenium
File: ch11_shell_17_creating_a_beautifulsoup_object_from_htm.py (17 of 34 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile)
type(exampleSoup)
# OUT: <class 'bs4.BeautifulSoup'>
