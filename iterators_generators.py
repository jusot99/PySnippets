# This program demonstrates different iterators and generators in Python.

# Using an iterator
numbers = [1, 2, 3, 4, 5]
iterator = iter(numbers)

print("Using an iterator:")
try:
    while True:
        element = next(iterator)
        print(element)
except StopIteration:
    print("Iterator exhausted.")

# Using an iterator with a for loop
print("\nUsing an iterator with a for loop:")
for number in iter(numbers):
    print(number)

# Custom iterator
class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        else:
            result = self.start
            self.start += 1
            return result

# Using a custom iterator
print("\nUsing a custom iterator:")
my_range = MyRange(1, 5)
for number in my_range:
    print(number)

# Using a generator function
def my_range_generator(start, end):
    while start < end:
        yield start
        start += 1

# Using a generator function
print("\nUsing a generator function:")
for number in my_range_generator(1, 5):
    print(number)

# Generator expression
generator_expression = (x**2 for x in range(5))

# Using a generator expression
print("\nUsing a generator expression:")
for square in generator_expression:
    print(square)

# Infinite generator
def infinite_count():
    count = 0
    while True:
        yield count
        count += 1

# Using an infinite generator
print("\nUsing an infinite generator:")
counter = infinite_count()
for _ in range(5):
    print(next(counter))
