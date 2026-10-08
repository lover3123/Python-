# Ch11 | 18/34 | Finding an Element with the select() Method [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter11

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

import bs4
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read())
elems = exampleSoup.select('#author')
type(elems)
# OUT: <class 'list'>
len(elems)
# OUT: 1
type(elems[0])
# OUT: <class 'bs4.element.Tag'>
elems[0].getText()
# OUT: 'Al Sweigart'
str(elems[0])
# OUT: '<span id="author">Al Sweigart</span>'
elems[0].attrs
# OUT: {'id': 'author'}
