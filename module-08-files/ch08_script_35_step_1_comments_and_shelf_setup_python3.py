"""Chapter 8: Reading and Writing Files
Section: Step 1: Comments and Shelf Setup
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter8
Type: book script/example
PPT map: Syllabus Ch8: files
File: ch08_script_35_step_1_comments_and_shelf_setup_python3.py (35 of 40 in this chapter)
"""

   #! python3
   # mcb.pyw - Saves and loads pieces of text to the clipboard.
 # Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
   #        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
   #        py.exe mcb.pyw list - Loads all keywords to clipboard.

 import shelve, pyperclip, sys

 mcbShelf = shelve.open('mcb')

   # TODO: Save clipboard content.

   # TODO: List keywords and load content.

   mcbShelf.close()
