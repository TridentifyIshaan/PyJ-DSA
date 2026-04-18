'''
> Date Created: 17/07/2025
> Author: Ishaan Rastogi
> Purpose: To demonstrate the use of sets in Python, including their properties, methods, and operations.
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

# Sets in Python
# A set is an unordered collection of unique elements.
# Sets are mutable & unindexed.

# Empty Set

# s = {}  # This creates an empty dictionary, not a set
s = set()  # Create an empty set

s = { 1, 5, 32, 54, 5, 5, 5, 34} # Duplicate elements are ignored in sets
print(s)  # Output: {32, 1, 34, 5, 54}
print()

# Non-homogeneous set
s = {1, 2, 3, 4, 5, "Ishaan", 5.6, True}
print(s)  # Output: {1, 2, 3, 4, 5, 'Ishaan', 5.6, True}
print(type(s))  # Output: <class 'set'>
print()

# Non-primitive set / Nested set - Sets can contain other sets
# s = {1, 2, 3, 4, 5, {6, 7, 8}, 5.6, True}
# print(s)  # Error: unhashable type: 'set'
# Sets can't contain other sets because sets are unhashable types. Attempting to create a set with another set as an element will raise a TypeError. Use a frozenset if you need to nest sets.

# Frozenset
# A frozenset is an immutable version of a set. It can be used as an element of another set or as a key in a dictionary.
fs = frozenset({1, 2, 3, 4, 5, 6, 7, 8, 9, 10})
print(fs)  # Output: frozenset({1, 2, 3, 4, 5, 6, 7, 8, 9, 10})
print(type(fs))  # Output: <class 'frozenset'>
print()

# Using frozenset in a set
s = {fs, 11, 12, 13}
print(s)  # Output: {frozenset({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}), 11, 12, 13}
print(type(s))  # Output: <class 'set'>
print()

# Using frozenset as a dictionary key
d = {fs: "Immutable Set"}
print(d)  # Output: {frozenset({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}): 'Immutable Set'}
print()

# Using frozenset as a value in a dictionary
fs = frozenset({1, 2, 3})
d = {"Immutable Set": fs}
print(d)  # Output: {'Immutable Set': frozenset({1, 2, 3})}
print()

# Ways to access elements in a frozenset
fs = frozenset({1, 2, 3})
print(list(fs))   # Output: [1, 2, 3]
print(set(fs))    # Output: {1, 2, 3}
print(*fs)        # Output: 1 2 3
print()

# * operator unpacks the elements of the frozenset, printing them as separate arguments.
# Usual purpose of * operator is to unpack elements in function calls or when printing.

# Note: frozensets do not support indexing or slicing like lists or tuples.
# You can convert a frozenset to a list or set to access its elements.

# Set Methods

# Set is mutable but can we change any value of the set?
# No, we cannot change the value of an element in a set directly.
# However, we can remove an element and add a new one.

# Adding elements to a set
s = {1, 2, 3}
s.add(4)  # Adds 4 to the set
print(s)  # Output: {1, 2, 3, 4}
print()

# Removing elements from a set
s.remove(2)  # Removes 2 from the set, raises KeyError if not found
print(s)  # Output: {1, 3, 4}
print()

# Discarding elements from a set
s.discard(2)  # Removes 3 from the set, does not raise an error if not found
print(s)  # Output: {1, 3, 4}
print()

# Popping an element from a set
popped_element = s.pop()  # Removes and returns an arbitrary element from the set
print(popped_element)  # Output: 1 (or another element, as sets are unordered)
print(s)  # Output: {3, 4}
print()

# Clearing a set
s.clear()  # Removes all elements from the set
print(s)  # Output: set()
print()

# Adding multiple elements to a set
s.update([5, 6, 7])  # Adds multiple elements from an iterable
print(s)  # Output: {5, 6, 7}
print()

# Deep copy - Change in original set does not affect the copy
s1 = {1, 2, 3}
s2 = s1.copy()  # Creates a shallow copy of the set
s1.add(4)  # Modifying the original set
print(s1)  # Output: {1, 2, 3, 4}
print(s2)  # Output: {1, 2, 3} (remains unchanged)
print()

# Shallow copy - Not applicable for sets as they are mutable
# Sets are mutable, so a deep copy is not necessary. A deep copy suffices.

# Set Operations

# Union of sets
s1 = {1, 2, 3}
s2 = {3, 4, 5}
U = s1.union(s2)  # or s1 | s2
print(U)  # Output: {1, 2, 3, 4, 5}
print()

# Intersection of sets
I = s1.intersection(s2)  # or s1 & s2
print(I)  # Output: {3}
print()

# Difference of sets
D = s1.difference(s2)  # or s1 - s2
print(D)  # Output: {1, 2}
print()

# Symmetric difference of sets - ( A - B ) U ( B - A )
S = s1.symmetric_difference(s2)  # or s1 ^ s2
print(S)  # Output: {1, 2, 4, 5}
print()

# Subset and Superset
# Checking if one set is a subset of another
s3 = {1, 2}
is_subset = s3.issubset(s1)  # or s3 <= s1
print(is_subset)  # Output: True
print()

# Checking if one set is a superset of another
is_superset = s1.issuperset(s3)  # or s1 >= s3
print(is_superset)  # Output: True
print()

# Disjoint sets - Two sets are disjoint if they have no elements in common
s4 = {6, 7}
is_disjoint = s1.isdisjoint(s4)  # or s1.isdisjoint(s2)
print(is_disjoint)  # Output: True (since {1, 2, 3} and {6, 7} have no common elements)
print()

# These type of things like this power set implementation will make you different from others and help you change your mindset will working on opensource projects or competitive programming.

# Power set - Set of all subsets of a set
# Python does not have a built-in method for power sets, but you can create one using itertools
from itertools import chain, combinations
def power_set(s):
    """Returns the power set of a given set."""
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)))

s5 = {1, 2, 3, 4, 5}
p_set = power_set(s5)
print(p_set)  # Output: [(), (1,), (2,), (3,), (4,), (5,), (1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5), (1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5), (1, 4, 5), (2, 3, 4), (2, 3, 5), (2, 4, 5), (3, 4, 5), (1, 2, 3, 4), (1, 2, 3, 5), (1, 2, 4, 5), (1, 3, 4, 5), (2, 3, 4, 5), (1, 2, 3, 4, 5)]
print()

# Membership testing
is_member = 3 in s5  # Returns True if 3 is in the set
print(is_member)  # Output: True
print()

# Iterating through a set - The only way to access elements in a set is through iteration because sets are unordered & unindexed.
for element in s5:
    print(element, end=' ')  # Output: 1 2 3 4 5
print()

# Although, we can calculate length of a set using len() function
length_of_set = len(s5)  # Returns the number of elements in the set
print(length_of_set)  # Output: 5
print()

# Type Conversion

# Converting a set to a list
s6 = list(s5)  # Converts the set to a list
print(s6)  # Output: [1, 2, 3, 4, 5]
print()

# Converting a set to a string
s7 = str(s5)  # Converts the set to a string
print(s7)  # Output: '{1, 2, 3, 4, 5}'
print()

# Converting a set to a tuple
s8 = tuple(s5)  # Converts the set to a tuple
print(s8)  # Output: (1, 2, 3, 4, 5)
print()

# Converting a set to a frozenset
s9 = frozenset(s5)  # Converts the set to a frozenset
print(s9)  # Output: frozenset({1, 2, 3, 4, 5})
print()

# Set comprehension
# Similar to list comprehension, you can create a set using set comprehension

s10 = {x**2 for x in range(1, 6)}  # Creates a set of squares of numbers from 1 to 5
print(s10)  # Output: {1, 4, 9, 16, 25}
print()

# Set comprehension with conditions
s11 = {x for x in range(1, 11) if x % 2 == 0}  # Creates a set of even numbers from 1 to 10
print(s11)  # Output: {2, 4, 6, 8, 10}
print()

# Set comprehension of frozenset
fs = frozenset({x for x in range(1, 11) if x % 2 == 0})
print(fs)  # Output: frozenset({2, 4, 6, 8, 10})
print(type(fs))  # Output: <class 'frozenset'>
print()