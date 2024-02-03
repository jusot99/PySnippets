# This program demonstrates different uses of lambda functions in Python.

# Basic lambda function
square = lambda x: x**2
print("Square of 4:", square(4))

# Lambda function with multiple parameters
add = lambda a, b: a + b
print("Sum of 3 and 5:", add(3, 5))

# Using lambda with built-in functions
numbers = [1, 2, 3, 4, 5]

# Map function with lambda
squared_numbers = list(map(lambda x: x**2, numbers))
print("Squared numbers:", squared_numbers)

# Filter function with lambda
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

# Reduce function with lambda (requires import from functools)
from functools import reduce

product_of_numbers = reduce(lambda x, y: x * y, numbers)
print("Product of numbers:", product_of_numbers)

# Sorting a list of tuples using lambda
students = [('Alice', 22), ('Bob', 19), ('Charlie', 25)]

# Sorting by age (index 1 in each tuple)
sorted_students_age = sorted(students, key=lambda x: x[1])
print("Sorted by age:", sorted_students_age)

# Sorting by name length (index 0 in each tuple)
sorted_students_name_length = sorted(students, key=lambda x: len(x[0]))
print("Sorted by name length:", sorted_students_name_length)

# Using lambda in higher-order functions
def operation_maker(operation):
    return lambda x, y: operation(x, y)

# Using lambda to create specific operations
add_operation = operation_maker(lambda a, b: a + b)
subtract_operation = operation_maker(lambda a, b: a - b)

print("Result of addition:", add_operation(10, 5))
print("Result of subtraction:", subtract_operation(10, 5))
