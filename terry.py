import math
import sys
from os import rename

import requests

print(sys.version)
print(sys.executable)

def greet(who_to_greet):
    greeting = "hello, {}".format(who_to_greet)
    return greeting