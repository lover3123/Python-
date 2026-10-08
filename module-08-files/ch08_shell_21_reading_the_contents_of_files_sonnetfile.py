"""Chapter 8: Reading and Writing Files
Section: Reading the Contents of Files
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter8
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch8: files
File: ch08_shell_21_reading_the_contents_of_files_sonnetfile.py (21 of 40 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

sonnetFile = open('sonnet29.txt')
sonnetFile.readlines()
# OUT: [When, in disgrace with fortune and men's eyes,\n', ' I all alone beweep my
# OUT: outcast state,\n', And trouble deaf heaven with my bootless cries,\n', And
# OUT: look upon myself and curse my fate,']
