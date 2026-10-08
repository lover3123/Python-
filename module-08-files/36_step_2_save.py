# Ch8 | 36/40 | Step 2: Save Clipboard Content with a Keyword [script]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter8

   #! python3
   # mcb.pyw - Saves and loads pieces of text to the clipboard.
   --snip--

   # Save clipboard content.
 if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
         mcbShelf[sys.argv[2]] = pyperclip.paste()
   elif len(sys.argv) == 2:
    # TODO: List keywords and load content.

   mcbShelf.close()
