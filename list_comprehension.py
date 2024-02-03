# This program demonstrates different list comprehensions in Python.

# Basic list comprehension
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers]
print("Squared numbers:", squared_numbers)

# List comprehension with condition
even_squares = [x**2 for x in numbers if x % 2 == 0]
print("Even squared numbers:", even_squares)

# Nested list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_matrix = [element for row in matrix for element in row]
print("Flattened matrix:", flattened_matrix)

# List comprehension with if-else condition
parity_labels = ["Even" if x % 2 == 0 else "Odd" for x in numbers]
print("Parity labels:", parity_labels)

# List comprehension for strings
words = ["apple", "banana", "cherry"]
capitalized_words = [word.capitalize() for word in words]
print("Capitalized words:", capitalized_words)

# List comprehension with enumerate
indexed_words = [(index, word) for index, word in enumerate(words)]
print("Indexed words:", indexed_words)

# List comprehension with zip
fruits = ["apple", "banana", "cherry"]
colors = ["red", "yellow", "red"]
fruit_color_pairs = [(fruit, color) for fruit, color in zip(fruits, colors)]
print("Fruit-color pairs:", fruit_color_pairs)

# List comprehension for filtering and transforming
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
filtered_squares = [x**2 for x in numbers if x % 2 == 0]
print("Filtered squares of even numbers:", filtered_squares)

# List comprehension with set
unique_lengths = {len(word) for word in words}
print("Unique lengths of words:", unique_lengths)

# List comprehension with dictionary
word_lengths = {word: len(word) for word in words}
print("Word lengths dictionary:", word_lengths)

# List comprehension with conditional expression
divisible_by_three = [x if x % 3 == 0 else "Not divisible" for x in numbers]
print("Divisible by three or 'Not divisible':", divisible_by_three)
