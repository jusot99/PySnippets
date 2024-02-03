# Type Hints Guide

# 1. Basic Type Hints

# Variables with type hints
name: str = "Alice"
age: int = 30
is_student: bool = False
salary: float = 50000.0

# Function with type hints
def greet_person(person_name: str, person_age: int) -> str:
    return f"Hello, {person_name}! Age: {person_age}"

# Calling the function
result = greet_person(name, age)
print(result)

# 2. Type Hints for Lists and Dicts

from typing import List, Dict, Union, Optional

# List with type hint
numbers: List[int] = [1, 2, 3, 4, 5]

# Dict with type hints for keys and values
user_data: Dict[str, Union[str, int]] = {'name': 'Bob', 'age': 25, 'is_student': True}

# 3. Type Hints for Functions

# Type hints for function parameters and return value
def calculate_sum(a: int, b: int) -> int:
    return a + b

# Calling the function with correct types
result_sum = calculate_sum(10, 20)
print("Sum:", result_sum)

# Calling the function with incorrect types (static analysis tool may catch this)
# result_sum_error = calculate_sum("a", "b")  # Uncommenting this line will raise a type error

# 4. Type Hints for Optional Values

from typing import Optional

# Optional type hint
def find_person(name: str) -> Optional[str]:
    # Function returns None if person is not found
    return name if name in ['Alice', 'Bob', 'Charlie'] else None

# 5. Type Hints for Any

from typing import Any

# Any type hint
def process_data(data: Any) -> str:
    return f"Processed: {data}"

# 6. Type Hints for Custom Classes

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

# Function with custom class type hint
def calculate_distance(point1: Point, point2: Point) -> float:
    return ((point1.x - point2.x)**2 + (point1.y - point2.y)**2)**0.5

# Creating instances of the custom class
point_a = Point(0, 0)
point_b = Point(3, 4)

# Calling the function with instances of the custom class
distance = calculate_distance(point_a, point_b)
print("Distance:", distance)

# Note: Type hints are not enforced at runtime but provide valuable information for static analysis tools and documentation.
