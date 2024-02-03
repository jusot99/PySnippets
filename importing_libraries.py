# This program demonstrates importing various libraries in Python.

# Import the math library
import math

# Use functions from the math library
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Sine of 30 degrees: {math.sin(math.radians(30))}")
print(f"Value of pi: {math.pi}")

# Import the random library
import random

# Use functions from the random library
random_number = random.randint(1, 10)
print(f"Random number between 1 and 10: {random_number}")

# Import the datetime library
import datetime

# Use functions from the datetime library
current_time = datetime.datetime.now()
print(f"Current date and time: {current_time}")

# Import a specific function from a library
from statistics import mean

# Use the mean function from the statistics library
numbers = [2, 4, 6, 8, 10]
average = mean(numbers)
print(f"Mean of the numbers: {average}")

# Import a library with an alias
import numpy as np

# Use functions from the numpy library
array = np.array([1, 2, 3, 4, 5])
print(f"Sum of the array elements: {np.sum(array)}")

# Importing a module from a package
from urllib.request import urlopen, URLError

try:
    # Use the urlopen function from the urllib library
    response = urlopen("https://www.example.com")
    html_content = response.read()
    print(f"Content from example.com: {html_content[:100]}")
except URLError as e:
    print(f"Error fetching URL: {e}")

# Import everything from a module (not recommended for large libraries)
from os import *

# Use functions and constants from the os module
current_directory = getcwd()
print(f"Current working directory: {current_directory}")

# Importing a custom module from the same directory
import my_module

# Use functions from the custom module
my_module.greet("Alice")

# Importing a module from a different directory (assuming it's in the Python path)
import sys
sys.path.append("/path/to/other/directory")

import other_module

# Use functions from the other module
other_module.say_hello("Bob")
