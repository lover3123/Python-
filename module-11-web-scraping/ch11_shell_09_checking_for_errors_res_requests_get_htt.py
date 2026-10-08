"""Chapter 11: Web Scraping
Section: Checking for Errors
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter11
Type: interactive-shell session (>>> stripped; expected output kept as comments)
PPT map: Syllabus Ch11: webbrowser, requests, bs4, selenium
File: ch11_shell_09_checking_for_errors_res_requests_get_htt.py (9 of 34 in this chapter)
"""

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
res.raise_for_status()
# OUT: Traceback (most recent call last):
# OUT:   File "<pyshell#138>", line 1, in <module>
# OUT:     res.raise_for_status()
# OUT:   File "C:\Python34\lib\site-packages\requests\models.py", line 773, in raise_for_status
# OUT:     raise HTTPError(http_error_msg, response=self)
# OUT: requests.exceptions.HTTPError: 404 Client Error: Not Found
