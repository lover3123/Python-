"""Chapter 11: Web Scraping
Section: Finding an Element with the select() Method
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter11
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch11: webbrowser, requests, bs4, selenium
File: ch11_shell_19_finding_an_element_with_the_select_metho.py (19 of 34 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

pElems = exampleSoup.select('p')
str(pElems[0])
# OUT: '<p>Download my <strong>Python</strong> book from <a href="http://
# OUT: inventwithpython.com">my website</a>.</p>'
pElems[0].getText()
# OUT: 'Download my Python book from my website.'
str(pElems[1])
# OUT: '<p class="slogan">Learn Python the easy way!</p>'
pElems[1].getText()
# OUT: 'Learn Python the easy way!'
str(pElems[2])
# OUT: '<p>By <span id="author">Al Sweigart</span></p>'
pElems[2].getText()
# OUT: 'By Al Sweigart'
