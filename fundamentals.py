# This is a simple Python program that takes user input for name and age.

# Step 1: Prompt the user to enter their name
name = input("Enter your name: ")

# Step 2: Prompt the user to enter their age
age = input("Enter your age: ")

# Step 3: Convert the age input to an integer
# Note: Input function returns a string, so we need to convert it to an integer.
age = int(age)

# Step 4: Print a message with the user's name and age
# Note: We use f-strings (formatted string literals) to insert variables into the string.
print(f"Hello, {name}! You are {age} years old.")
