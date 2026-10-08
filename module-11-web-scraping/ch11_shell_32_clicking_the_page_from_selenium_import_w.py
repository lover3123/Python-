"""Chapter 11: Web Scraping
Section: Clicking the Page
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter11
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch11: webbrowser, requests, bs4, selenium
File: ch11_shell_32_clicking_the_page_from_selenium_import_w.py (32 of 34 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')
linkElem = browser.find_element_by_link_text('Read It Online')
type(linkElem)
# OUT: <class 'selenium.webdriver.remote.webelement.WebElement'>
linkElem.click() # follows the "Read It Online" link
