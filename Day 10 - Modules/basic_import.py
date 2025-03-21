# Import entire module
import math
print(f"Square root of 16: {math.sqrt(16)}")

# Import specific items
from random import randint
print(f"Random number: {randint(1, 100)}")

# Alias imports
import datetime as dt
print(f"Current year: {dt.datetime.now().year}")