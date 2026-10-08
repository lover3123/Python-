"""Chapter 8: Reading and Writing Files
Section: Writing to Files
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter8
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch8: files
File: ch08_shell_22_writing_to_files_baconfile_open_bacon_tx.py (22 of 40 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

baconFile = open('bacon.txt', 'w')
baconFile.write('Hello world!\n')
# OUT: 13
baconFile.close()
baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')
# OUT: 25
baconFile.close()
baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)
# OUT: Hello world!
# OUT: Bacon is not a vegetable.
