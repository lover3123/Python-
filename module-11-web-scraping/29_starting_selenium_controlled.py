# Ch11 | 29/34 | Starting a Selenium-Controlled Browser [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter11

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

from selenium import webdriver
browser = webdriver.Firefox()
type(browser)
# OUT: <class 'selenium.webdriver.firefox.webdriver.WebDriver'>
browser.get('http://inventwithpython.com')
