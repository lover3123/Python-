"""Chapter 16: Sending Email and Text Messages
Section: Starting TLS Encryption
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter16
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch16: smtplib, imap, twilio
File: ch16_shell_05_starting_tls_encryption_smtpobj_starttls.py (5 of 36 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

smtpObj.starttls()
# OUT: (220, b'2.0.0 Ready to start TLS')
