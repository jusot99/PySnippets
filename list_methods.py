# This program demonstrates a representative sample of list methods in Python.

# 1. Creating a list
original_list = [1, 2, 3, 4, 5]

# 2. Adding elements
original_list.append(6)
print("After append:", original_list)

original_list.extend([7, 8, 9])
print("After extend:", original_list)

original_list.insert(3, 10)
print("After insert:", original_list)

# 3. Removing elements
original_list.remove(5)
print("After remove:", original_list)

popped_element = original_list.pop(2)
print("Popped element:", popped_element)
print("After pop:", original_list)

original_list.clear()
print("After clear:", original_list)

# 4. Copying and cloning
original_list = [1, 2, 3, 4, 5]
shallow_copy = original_list.copy()
print("Shallow copy:", shallow_copy)

deep_copy = original_list[:]
print("Deep copy:", deep_copy)

# 5. Searching and counting
index_of_element = original_list.index(3)
print("Index of element:", index_of_element)

count_of_element = original_list.count(3)
print("Count of element:", count_of_element)

# 6. Sorting and reversing
original_list.sort()
print("Sorted list:", original_list)

original_list.reverse()
print("Reversed list:", original_list)

# 7. Slicing
sliced_list = original_list[1:4]
print("Sliced list:", sliced_list)

# 8. Modifying elements
original_list[2] = 100
print("After modification:", original_list)

# 9. Combining lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print("Combined list:", combined_list)

# 10. Removing duplicates
duplicated_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(duplicated_list))
print("List with duplicates removed:", unique_list)

# Note: This is just a small selection of list methods. Python has many more list methods that you can explore in the documentation.
