# This program demonstrates different types of operators in Python.

# Arithmetic operators
num1 = 10
num2 = 3
sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2
quotient_result = num1 / num2
remainder_result = num1 % num2
power_result = num1 ** num2

print(f"Arithmetic Operators: Sum = {sum_result}, Difference = {difference_result}, Product = {product_result}, Quotient = {quotient_result}, Remainder = {remainder_result}, Power = {power_result}")

# Comparison operators
greater_than = num1 > num2
less_than = num1 < num2
equal_to = num1 == num2
not_equal_to = num1 != num2
greater_than_or_equal = num1 >= num2
less_than_or_equal = num1 <= num2

print(f"Comparison Operators: Greater Than = {greater_than}, Less Than = {less_than}, Equal To = {equal_to}, Not Equal To = {not_equal_to}, Greater Than or Equal To = {greater_than_or_equal}, Less Than or Equal To = {less_than_or_equal}")

# Logical operators
logical_and = (num1 > 5) and (num2 < 5)
logical_or = (num1 > 5) or (num2 < 5)
logical_not = not (num1 > num2)

print(f"Logical Operators: Logical AND = {logical_and}, Logical OR = {logical_or}, Logical NOT = {logical_not}")

# Assignment operators
assignment_result = 5
assignment_result += 2
assignment_result -= 1
assignment_result *= 3
assignment_result /= 2

print(f"Assignment Operators: Result = {assignment_result}")

# Identity operators
identity_is = num1 is num2
identity_is_not = num1 is not num2

print(f"Identity Operators: is = {identity_is}, is not = {identity_is_not}")

# Membership operators
membership_in = num1 in [1, 2, 3, 10]
membership_not_in = num2 not in [1, 2, 3, 10]

print(f"Membership Operators: in = {membership_in}, not in = {membership_not_in}")
