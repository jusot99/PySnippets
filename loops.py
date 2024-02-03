# This program demonstrates different types of loops in Python.

# While loop
counter = 0
while counter < 5:
    print(f"While loop iteration {counter}")
    counter += 1

# For loop with range
for i in range(5):
    print(f"For loop iteration {i}")

# For loop with iterable (list)
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"For loop with iterable: {fruit}")

# Nested loops
for i in range(3):
    for j in range(2):
        print(f"Nested loop iteration: ({i}, {j})")

# Break statement
for i in range(10):
    print(f"Break statement: {i}")
    if i == 5:
        break

# Continue statement
for i in range(6):
    if i == 3:
        continue
    print(f"Continue statement: {i}")

# Looping through dictionary
person_info = {"name": "John", "age": 30, "city": "New York"}
for key, value in person_info.items():
    print(f"Dictionary iteration: {key} - {value}")

# Enumerate function
for index, fruit in enumerate(fruits):
    print(f"Enumerate function: Index {index}, Fruit {fruit}")

# While loop with else
counter = 0
while counter < 3:
    print(f"While loop with else: Iteration {counter}")
    counter += 1
else:
    print("While loop with else: Loop completed successfully.")

# For loop with else
for i in range(3):
    print(f"For loop with else: Iteration {i}")
else:
    print("For loop with else: Loop completed successfully.")
