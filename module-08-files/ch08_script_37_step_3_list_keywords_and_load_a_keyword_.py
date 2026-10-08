"""Chapter 8: Reading and Writing Files
Section: Step 3: List Keywords and Load a Keyword’s Content
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter8
Type: book script/example
PPT map: Syllabus Ch8: files
File: ch08_script_37_step_3_list_keywords_and_load_a_keyword_.py (37 of 40 in this chapter)
"""

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
