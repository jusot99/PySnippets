# abs() - Returns the absolute value of a number
def abs_example():
    result = abs(-10)
    print(f"abs(-10) = {result}")

# all() - Returns True if all elements of the iterable are true
def all_example():
    result = all([True, True, False])
    print(f"all([True, True, False]) = {result}")

# any() - Returns True if any element of the iterable is true
def any_example():
    result = any([False, False, True])
    print(f"any([False, False, True]) = {result}")

# bin() - Converts an integer to a binary string
def bin_example():
    result = bin(10)
    print(f"bin(10) = {result}")

# sorted() - Returns a sorted list from the specified iterable
def sorted_example():
    result = sorted([3, 1, 4, 1, 5, 9, 2, 6, 5])
    print(f"sorted([3, 1, 4, 1, 5, 9, 2, 6, 5]) = {result}")

# sum() - Returns the sum of all items in an iterable
def sum_example():
    result = sum([1, 2, 3, 4, 5])
    print(f"sum([1, 2, 3, 4, 5]) = {result}")

# type() - Returns the type of an object
def type_example():
    result = type("Hello, World!")
    print(f"type('Hello, World!') = {result}")

# zip() - Returns an iterator of tuples, where the first item in each passed iterator is paired together
def zip_example():
    result = list(zip([1, 2, 3], ['a', 'b', 'c']))
    print(f"list(zip([1, 2, 3], ['a', 'b', 'c'])) = {result}")

# Example usage of each function
abs_example()
all_example()
any_example()
bin_example()
sorted_example()
sum_example()
type_example()
zip_example()
