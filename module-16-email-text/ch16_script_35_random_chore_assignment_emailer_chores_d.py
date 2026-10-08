"""Chapter 16: Sending Email and Text Messages
Section: Random Chore Assignment Emailer
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter16
Type: book script/example
PPT map: Syllabus Ch16: smtplib, imap, twilio
File: ch16_script_35_random_chore_assignment_emailer_chores_d.py (35 of 36 in this chapter)
"""

chores = ['dishes', 'bathroom', 'vacuum', 'walk dog']
randomChore = random.choice(chores)
chores.remove(randomChore) # this chore is now taken, so remove it
