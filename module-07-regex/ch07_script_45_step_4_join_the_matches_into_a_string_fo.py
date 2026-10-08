"""Chapter 7: Pattern Matching with Regular Expressions
Section: Step 4: Join the Matches into a String for the Clipboard
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter7
Type: book script/example
PPT map: Syllabus Ch7: regex
File: ch07_script_45_step_4_join_the_matches_into_a_string_fo.py (45 of 46 in this chapter)
"""

#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

--snip--
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
