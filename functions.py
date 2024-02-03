# This program demonstrates different aspects of functions in Python.

# Function without parameters and return value
def greet():
    print("Hello, welcome!")

greet()

# Function with parameters
def add_numbers(a, b):
    return a + b

result = add_numbers(3, 5)
print(f"Sum of numbers: {result}")

# Default parameter values
def power(base, exponent=2):
    return base ** exponent

result_default = power(3)
result_custom = power(3, 4)
print(f"Default power: {result_default}, Custom power: {result_custom}")

# Variable number of arguments
def print_args(*args):
    for arg in args:
        print(arg)

print_args(1, "two", 3.0, [4, 5])

# Keyword arguments
def print_info(name, age):
    print(f"Name: {name}, Age: {age}")

print_info(name="John", age=25)

# Return multiple values
def calculate_values(x, y):
    sum_result = x + y
    product_result = x * y
    return sum_result, product_result

sum_result, product_result = calculate_values(2, 3)
print(f"Sum: {sum_result}, Product: {product_result}")

# Lambda functions (anonymous functions)
square = lambda x: x**2
print(f"Square of 4: {square(4)}")

# Recursive function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(f"Factorial of 5: {factorial(5)}")

# Function with docstring
def example_function():
    """
    This is a docstring that provides information about the function.
    It can be accessed using the help() function.
    """
    print("This is an example function.")

# Accessing docstring using help()
help(example_function)
