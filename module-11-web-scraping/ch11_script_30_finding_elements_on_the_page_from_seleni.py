"""Chapter 11: Web Scraping
Section: Finding Elements on the Page
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter11
Type: book script/example
PPT map: Syllabus Ch11: webbrowser, requests, bs4, selenium
File: ch11_script_30_finding_elements_on_the_page_from_seleni.py (30 of 34 in this chapter)
"""

from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')
try:
    elem = browser.find_element_by_class_name('bookcover')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')
