# Ch11 | 09/34 | Checking for Errors [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter11

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
