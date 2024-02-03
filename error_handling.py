# This program demonstrates error handling in Python.

# Division by zero error
def divide_numbers(a, b):
    try:
        result = a / b
        print(f"Result of division: {result}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        print("Cannot divide by zero.")

# Call the function with different values
divide_numbers(10, 2)
divide_numbers(5, 0)

# Handling multiple exceptions
def handle_exceptions(value):
    try:
        # Attempt to convert the input to an integer
        result = int(value)
        print(f"Successfully converted to integer: {result}")
    except ValueError as ve:
        print(f"ValueError: {ve}")
        print("Invalid input. Please enter a valid integer.")
    except TypeError as te:
        print(f"TypeError: {te}")
        print("Invalid type. Please enter a valid integer.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print("No exception occurred.")

# Call the function with different inputs
handle_exceptions("123")
handle_exceptions("abc")
handle_exceptions([1, 2, 3])

# Using the finally block
def divide_and_log(a, b):
    try:
        result = a / b
        print(f"Result of division: {result}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        print("Cannot divide by zero.")
    finally:
        print("This block always executes, regardless of whether an exception occurred.")

# Call the function with different values
divide_and_log(8, 2)
divide_and_log(5, 0)

# Raising custom exceptions
def validate_age(age):
    try:
        if not isinstance(age, int):
            raise ValueError("Age must be an integer.")
        if age < 0 or age > 120:
            raise ValueError("Age must be between 0 and 120.")
        print(f"Valid age: {age}")
    except ValueError as ve:
        print(f"Validation Error: {ve}")

# Call the function with different age values
validate_age(25)
validate_age("abc")
validate_age(150)
