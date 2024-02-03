# This program demonstrates a representative sample of set methods in Python.

# 1. Creating sets
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# 2. Adding and removing elements
set1.add(6)
print("After add:", set1)

set1.update({7, 8, 9})
print("After update:", set1)

set1.remove(2)
print("After remove:", set1)

# 3. Set operations
union_set = set1.union(set2)
print("Union of sets:", union_set)

intersection_set = set1.intersection(set2)
print("Intersection of sets:", intersection_set)

difference_set = set1.difference(set2)
print("Difference of sets:", difference_set)

symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric difference of sets:", symmetric_difference_set)

# 4. Checking subsets and supersets
is_subset = set2.issubset(set1)
print("Is set2 a subset of set1?", is_subset)

is_superset = set1.issuperset(set2)
print("Is set1 a superset of set2?", is_superset)

# 5. Checking disjoint sets
are_disjoint = set1.isdisjoint(set2)
print("Are set1 and set2 disjoint?", are_disjoint)

# 6. Copying and clearing
shallow_copy = set1.copy()
print("Shallow copy:", shallow_copy)

set1.clear()
print("After clear:", set1)

# 7. Discarding elements
set2.discard(6)
print("After discard:", set2)

# 8. Pop from set
popped_element = set2.pop()
print("Popped element:", popped_element)

# 9. Frozenset (immutable set)
frozen_set = frozenset({1, 2, 3, 4})
print("Frozen set:", frozen_set)

# 10. Set comprehension
set3 = {x**2 for x in range(5)}
print("Set comprehension:", set3)

# Note: This is just a small selection of set methods. Python has many more set methods that you can explore in the documentation.
