# Ch10 | 12/24 | Using an Assertion in a Traffic Light Simulation [script]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter10

   Traceback (most recent call last):
     File "carSim.py", line 14, in <module>
       switchLights(market_2nd)
     File "carSim.py", line 13, in switchLights
       assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)
 AssertionError: Neither light is red! {'ns': 'yellow', 'ew': 'green'}
