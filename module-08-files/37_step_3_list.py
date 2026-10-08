# Ch8 | 37/40 | Step 3: List Keywords and Load a Keyword’s Content [script]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter8

   #! python3
   # mcb.pyw - Saves and loads pieces of text to the clipboard.
   --snip--

   # Save clipboard content.
   if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
           mcbShelf[sys.argv[2]] = pyperclip.paste()
   elif len(sys.argv) == 2:
       # List keywords and load content.
     if sys.argv[1].lower() == 'list':
         pyperclip.copy(str(list(mcbShelf.keys())))
       elif sys.argv[1] in mcbShelf:
         pyperclip.copy(mcbShelf[sys.argv[1]])

   mcbShelf.close()
