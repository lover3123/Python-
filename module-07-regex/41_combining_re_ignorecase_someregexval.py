# Ch7 | 41/46 | Combining re.IGNORECASE, re.DOTALL, and re.VERBOSE [shell]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter7

# Interactive session from the book. Run line-by-line in IDLE.
# Lines starting with >>> are input; other lines are expected output (commented).

someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
