"""Chapter 10: Debugging
Section: Using an Assertion in a Traffic Light Simulation
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter10
Type: book script/example
PPT map: Syllabus Ch10: raise, assert, logging, debugger
File: ch10_script_12_using_an_assertion_in_a_traffic_light_si.py (12 of 24 in this chapter)
"""

   Traceback (most recent call last):
     File "carSim.py", line 14, in <module>
       switchLights(market_2nd)
     File "carSim.py", line 13, in switchLights
       assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)
 AssertionError: Neither light is red! {'ns': 'yellow', 'ew': 'green'}
