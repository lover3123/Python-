# Ch11 | 20/34 | Getting Data from an Element’s Attributes [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter11

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
