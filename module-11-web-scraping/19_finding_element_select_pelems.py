# Ch11 | 19/34 | Finding an Element with the select() Method [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter11

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
