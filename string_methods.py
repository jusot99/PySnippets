# This program demonstrates a representative sample of string methods in Python.

# 1. Creating a string
original_string = "Hello, Python!"

# 2. Accessing characters
print("First character:", original_string[0])
print("Last character:", original_string[-1])

# 3. Checking string properties
print("Is the string alphanumeric?", original_string.isalnum())
print("Is the string alphabetic?", original_string.isalpha())
print("Is the string lowercase?", original_string.islower())
print("Is the string uppercase?", original_string.isupper())
print("Is the string a titlecased string?", original_string.istitle())
print("Is the string a decimal string?", original_string.isdecimal())

# 4. Modifying the case of the string
print("Lowercase:", original_string.lower())
print("Uppercase:", original_string.upper())
print("Titlecase:", original_string.title())
print("Swapcase:", original_string.swapcase())

# 5. Searching within a string
substring = "Py"
print("Index of substring:", original_string.find(substring))
print("Index of substring (case insensitive):", original_string.lower().find(substring.lower()))
print("Count occurrences of substring:", original_string.count(substring))

# 6. Checking and modifying the content
print("Does the string start with 'Hello'?", original_string.startswith("Hello"))
print("Does the string end with 'Python'?", original_string.endswith("Python"))
modified_string = original_string.replace("Python", "World")
print("String after replacement:", modified_string)

# 7. Splitting and joining
words = original_string.split(", ")
print("List of words:", words)
new_string = "-".join(words)
print("String after joining with '-':", new_string)

# 8. Stripping whitespace
whitespace_string = "   leading and trailing   "
print("Stripped whitespace:", whitespace_string.strip())

# 9. Formatting strings
name = "Alice"
age = 25
formatted_string = "Name: {}, Age: {}".format(name, age)
print("Formatted string:", formatted_string)

# 10. Checking characters
print("Are all characters alphabetic?", original_string.isalpha())
print("Are all characters digits?", original_string.isdigit())
print("Are all characters printable?", original_string.isprintable())

# 11. Length of the string
print("Length of the string:", len(original_string))

# Note: This is just a small selection of string methods. Python has many more string methods that you can explore in the documentation.
