"""Chapter 10: Debugging
Section: Using an Assertion in a Traffic Light Simulation
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter10
Type: book script/example
PPT map: Syllabus Ch10: raise, assert, logging, debugger
File: ch10_script_11_using_an_assertion_in_a_traffic_light_si.py (11 of 24 in this chapter)
"""

assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)
