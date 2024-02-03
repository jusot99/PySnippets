# This program demonstrates different types of conditional statements in Python.

# If statement
number = 15

if number > 10:
    print("Number is greater than 10.")
elif number == 10:
    print("Number is equal to 10.")
else:
    print("Number is less than 10.")

# Nested if statement
if number > 5:
    print("Number is greater than 5.")
    if number % 2 == 0:
        print("Number is even.")
    else:
        print("Number is odd.")
else:
    print("Number is 5 or less.")

# Ternary conditional expression
is_even = True if number % 2 == 0 else False
print(f"The number is {'even' if is_even else 'odd'}.")

# Switch-case statement (using a dictionary)
def switch_case(argument):
    switch_dict = {
        1: "Case 1",
        2: "Case 2",
        3: "Case 3",
        "default": "Default Case"
    }
    return switch_dict.get(argument, switch_dict["default"])

print(switch_case(2))
print(switch_case(5))

# Membership test
list_of_numbers = [1, 2, 3, 4, 5]

if number in list_of_numbers:
    print(f"{number} is in the list.")
else:
    print(f"{number} is not in the list.")

# Logical operators with conditionals
logical_and_condition = (number > 5) and (number < 20)
logical_or_condition = (number < 5) or (number > 10)

if logical_and_condition:
    print("Number is between 5 and 20.")

if logical_or_condition:
    print("Number is less than 5 or greater than 10.")
