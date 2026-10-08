"""Chapter 8: Reading and Writing Files
Section: Step 2: Save Clipboard Content with a Keyword
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter8
Type: book script/example
PPT map: Syllabus Ch8: files
File: ch08_script_36_step_2_save_clipboard_content_with_a_key.py (36 of 40 in this chapter)
"""

   #! python3
   # mcb.pyw - Saves and loads pieces of text to the clipboard.
   --snip--

   # Save clipboard content.
 if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
         mcbShelf[sys.argv[2]] = pyperclip.paste()
   elif len(sys.argv) == 2:
    # TODO: List keywords and load content.

   mcbShelf.close()
