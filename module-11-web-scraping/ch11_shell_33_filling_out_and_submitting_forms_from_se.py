"""Chapter 11: Web Scraping
Section: Filling Out and Submitting Forms
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter11
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch11: webbrowser, requests, bs4, selenium
File: ch11_shell_33_filling_out_and_submitting_forms_from_se.py (33 of 34 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

from selenium import webdriver
browser = webdriver.Firefox()
browser.get('https://mail.yahoo.com')
emailElem = browser.find_element_by_id('login-username')
emailElem.send_keys('not_my_real_email')
passwordElem = browser.find_element_by_id('login-passwd')
passwordElem.send_keys('12345')
passwordElem.submit()
