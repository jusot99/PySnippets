# This program demonstrates a representative sample of built-in functions in Python.

# 1. Mathematical functions
num_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print("Sum of numbers:", sum(num_list))
print("Minimum value:", min(num_list))
print("Maximum value:", max(num_list))
print("Absolute value:", abs(-7.5))
print("Rounded value:", round(7.8))

# 2. Type conversion functions
num_str = "123"
print("Integer conversion:", int(num_str))
print("Float conversion:", float(num_str))
print("String conversion:", str(456))

# 3. String manipulation functions
text = "   Hello, World!   "
print("Length of string:", len(text))
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Strip whitespace:", text.strip())
print("Replace substring:", text.replace("World", "Python"))
print("Is digit:", text.isdigit())

# 4. List functions
my_list = [1, 2, 3, 4, 5]
print("Length of list:", len(my_list))
print("Sum of list:", sum(my_list))
print("Sorted list:", sorted(my_list))
print("Reversed list:", list(reversed(my_list)))

# 5. Dictionary functions
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("Keys:", my_dict.keys())
print("Values:", my_dict.values())
print("Items:", my_dict.items())
print("Get value with default:", my_dict.get('d', 'Not Found'))

# 6. Input/output functions
user_input = input("Enter something: ")
print("You entered:", user_input)

# 7. Miscellaneous functions
print("Type of an object:", type(num_list))
print("ID of an object:", id(num_list))
print("Check if object is iterable:", hasattr(num_list, '__iter__'))
print("Evaluate an expression:", eval("3 + 4 * 2"))

# Note: This is just a small selection of built-in functions. Python has many more built-in functions that you can explore in the documentation.
