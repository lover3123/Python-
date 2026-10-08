"""Chapter 8: Reading and Writing Files
Section: Saving Variables with the shelve Module
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter8
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch8: files
File: ch08_shell_25_saving_variables_with_the_shelve_module_.py (25 of 40 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

shelfFile = shelve.open('mydata')
list(shelfFile.keys())
# OUT: ['cats']
list(shelfFile.values())
# OUT: [['Zophie', 'Pooka', 'Simon']]
shelfFile.close()
