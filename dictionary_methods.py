# This program demonstrates a representative sample of dictionary methods in Python.

# 1. Creating a dictionary
original_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# 2. Accessing elements
print("Value for 'name':", original_dict['name'])
print("Value for 'age' using get:", original_dict.get('age'))
print("All keys:", original_dict.keys())
print("All values:", original_dict.values())
print("All key-value pairs:", original_dict.items())

# 3. Modifying elements
original_dict['age'] = 26
print("After modification:", original_dict)

# 4. Adding elements
original_dict['gender'] = 'Female'
print("After addition:", original_dict)

# 5. Removing elements
removed_value = original_dict.pop('age')
print("Removed value:", removed_value)
print("After pop:", original_dict)

del original_dict['city']
print("After delete:", original_dict)

original_dict.clear()
print("After clear:", original_dict)

# 6. Copying and updating
shallow_copy = original_dict.copy()
print("Shallow copy:", shallow_copy)

new_dict = {'country': 'USA'}
original_dict.update(new_dict)
print("After update:", original_dict)

# 7. Searching and checking
print("Is 'name' in keys?", 'name' in original_dict)
print("Is 'gender' in keys?", 'gender' in original_dict)

# 8. Getting and setting default values
default_value = original_dict.get('height', 'Not available')
print("Default value for 'height':", default_value)

original_dict.setdefault('height', 170)
print("After setdefault:", original_dict)

# 9. Populating a dictionary using fromkeys
keys = ['a', 'b', 'c']
default_value = 0
new_dict = dict.fromkeys(keys, default_value)
print("Dictionary from keys:", new_dict)

# 10. Merging dictionaries using update (Python 3.9+)
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = dict1 | dict2
print("Merged dictionary:", merged_dict)

# Note: This is just a small selection of dictionary methods. Python has many more dictionary methods that you can explore in the documentation.
