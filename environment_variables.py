# Environment Variables Guide

import os

# 1. Setting Environment Variables
# Note: Environment variables can be set in the terminal or command prompt before running the script.
# Example (Windows): set MY_VARIABLE=value
# Example (Linux/Mac): export MY_VARIABLE=value

# Alternatively, you can set environment variables within the script using os.environ:
os.environ['MY_VARIABLE'] = 'value'

# 2. Accessing Environment Variables
# Use the os.environ dictionary to access environment variables:

my_variable = os.environ.get('MY_VARIABLE')

if my_variable:
    print(f"MY_VARIABLE is set to: {my_variable}")
else:
    print("MY_VARIABLE is not set")

# 3. Default Values for Environment Variables
# You can use the get method with a default value to avoid raising an exception if the variable is not set:

default_value = os.environ.get('NON_EXISTENT_VARIABLE', 'default')
print(f"NON_EXISTENT_VARIABLE is set to: {default_value}")

# 4. Checking if an Environment Variable is Set
# Use the 'in' operator to check if an environment variable is set:

if 'ANOTHER_VARIABLE' in os.environ:
    print(f"ANOTHER_VARIABLE is set to: {os.environ['ANOTHER_VARIABLE']}")
else:
    print("ANOTHER_VARIABLE is not set")

# 5. Unsetting an Environment Variable
# Use the pop method to remove an environment variable:

if 'TO_BE_UNSET' in os.environ:
    unset_value = os.environ.pop('TO_BE_UNSET')
    print(f"TO_BE_UNSET was set to: {unset_value}")
else:
    print("TO_BE_UNSET is not set")

# Note: Environment variables are typically used for configuration settings and sensitive information.
# Be cautious about storing sensitive information in environment variables.
