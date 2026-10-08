# Ch8 | 35/40 | Step 1: Comments and Shelf Setup [script]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter8

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
