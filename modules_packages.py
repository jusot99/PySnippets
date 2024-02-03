# Modules and Packages Guide

# 1. Creating a Module

# File: my_module.py
# Content:
"""
def greet(name):
    print(f"Hello, {name}!")
"""

# 2. Using the Module

# Importing the entire module
import my_module

my_module.greet("Alice")

# Importing specific functions from the module
from my_module import greet

greet("Bob")

# 3. Creating a Package

# Folder: my_package
# Files:
#   - __init__.py (empty file to indicate it's a package)
#   - module1.py
#   - module2.py

# File: my_package/__init__.py

# File: my_package/module1.py
"""
def func1():
    print("Function 1 from module1")
"""

# File: my_package/module2.py
"""
def func2():
    print("Function 2 from module2")
"""

# 4. Using the Package

# Importing modules from the package
from my_package import module1, module2

module1.func1()
module2.func2()

# 5. Aliasing Modules and Packages

# Aliasing a module
import my_module as mm

mm.greet("Charlie")

# Aliasing a package
import my_package as mp

mp.module1.func1()

# 6. Using Third-Party Modules

# Install a third-party module using pip before using it
# Example: pip install requests

import requests

response = requests.get("https://www.example.com")
print("Status Code:", response.status_code)

# Note: Modules and packages are fundamental for organizing and reusing code in Python. 
# Explore the Python Standard Library and third-party libraries for a wide range of functionalities.
