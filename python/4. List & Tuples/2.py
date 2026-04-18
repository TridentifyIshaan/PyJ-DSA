'''
> Date Created: 14/07/2025
> Author: Ishaan Rastogi
> Purpose: To demonstrate the use of tuples in Python, including their properties, methods, and operations.
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

# Tuples in Python
# A tuple is a collection which is ordered and immutable. Allows duplicate members.

# Creating a tuple with same datatypes
a = (1, 2, 5, 6)
print(type(a))  # Output: <class 'tuple'>
print() # either print() or print("\n") can be used to add a new line

# empty tuple

a = ()
print(type(a))  # Output: <class 'tuple'>
print()

# It's just an integer
a = (1)
print(type(a))  # Output: <class 'int'> (not a tuple, just an integer)
print()

# Single element tuple
a = (1,)  # Note the comma
print(type(a))  # Output: <class 'tuple'>
print()

# Creating a tuple with different datatypes
a = (1, 2.5, "Hello", True)
print(type(a))  # Output: <class 'tuple'>
print()

# a[0] = 5 # Error -> Immutable

# Tuple methods

a = (1, 45, 342, 3424, False, 45, "Rohan")
print()

# Count method
print(a.count(45))  # Output: 2 (counts occurrences of 45)
print()

# Index method
print(a.index(342))  # Output: 2 (returns the index of the first occurrence of 342)
print()
# print(a.index(40)) -> Raises ValueError: 40 is not in tuple

# Slicing a tuple
print(a[0:3])  # Output: (1, 45, 342)
print(a[2:])   # Output: (342, 3424, False, 45, 'Rohan')
print(a[:3])   # Output: (1, 45, 342)
print(a[-1])   # Output: 'Rohan' (last element)
print(a[-2])   # Output: 45 (second last element)
print()

# Concatenation of tuples
b = (1, 2, 3)
c = (4, 5, 6)
print(b+c) # Output: (1, 2, 3, 4, 5, 6)
print()

# Adding corresponding elements of two tuples

# Note: Tuples are immutable, so we create a new tuple for the result and we achieve this using a generator expression, it works similarly to list comprehensions
d = tuple(b[i] + c[i] for i in range(len(b)))
print(d)  # Output: (5, 7, 9)
print()

# Repetition of tuples
print(b*3) # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)
print()

# Length of a tuple
print(len(b))  # Output: 3 (number of elements in tuple b)
print()

# Membership test
print(2 in b)  # Output: True (2 is in tuple b)
print(7 in b)  # Output: False (7 is not in tuple b)
print()

# Iterating through a tuple
for item in a:
    print(item, end=", ")  # Output: 1 45 342 3424 False 45 Rohan
    # end parameter is used to seperate items with a comma and space instead of a newline
print()

# Min and Max in a tuple
print(min(b))  # Output: 1 (minimum value in tuple b)
print(max(b))  # Output: 3 (maximum value in tuple b)
print()



# Nested tuples
nested_tuple = (1, 2, (3, 4), (5, 6))
print(nested_tuple)  # Output: (1, 2, (3, 4), (5, 6))
print(nested_tuple[2])  # Output: (3, 4) (accessing the nested tuple)
print(nested_tuple[2][1])  # Output: 4 (accessing an element in the nested tuple)
print()

# Tuple unpacking - assigning tuple elements to variables
x, y, z = (1, 2, 3)
print(x)  # Output: 1
print(y)  # Output: 2
print(z)  # Output: 3
print()

# Tuple unpacking with nested tuples
a, (b, c) = (1, (2, 3))
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3
print()