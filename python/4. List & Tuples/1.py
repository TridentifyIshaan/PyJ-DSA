'''
> Date Created: 25/04/2026
> Author: Ishaan Rastogi
> Purpose: To demonstrate the use of lists in Python, including their properties, methods, and operations.
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

# Lists are ordered collections that can hold multiple items of different data types

friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]

# Accessing elements in a list & slicing
print(friends, "\n")  # Output: ['Apple', 'Orange', 5, 345.06, False, 'Aakash', 'Rohan']
print(friends[0], "\n")  # Output: Apple (first element)
print(friends[1:4], "\n")  # Output: ['Orange', 5, 345.06] (slicing from index 1 to 3)
print(friends[-1], "\n")  # Output: Rohan (last element)

#List is mutable, meaning it can be changed after creation
friends[0]="Grapes"  # Changing the first element
print(friends, "\n")  # Output: ['Grapes', 'Orange', 5, 345.06, False, 'Aakash', 'Rohan']

# List methods

# Adding elements to a list
friends.append("Mango")  # Adding 'Mango' to the end of the list
print(friends, "\n")  # Output: ['Grapes', 'Orange', 5, 345.06, False, 'Aakash', 'Rohan', 'Mango']

# Removing elements from a list
friends.remove("Orange")  # Removing 'Orange' from the list
print(friends, "\n")  # Output: ['Grapes', 5, 345.06, False, 'Aakash', 'Rohan', 'Mango']

# Inserting elements at a specific position
friends.insert(1, "Banana")  # Inserting 'Banana' at index 1
print(friends, "\n")  # Output: ['Grapes', 'Banana', 5, 345.06, False, 'Aakash', 'Rohan', 'Mango']

# List can have multiple data types 
l0 = [1, "Hello", 345.06, True, "Ishaan"]
print(type(l0[3]), "\n") # output <class 'bool'>

# Sorting a list
# Note: Sorting works only for lists with elements of the same data type

l1 = [5, 2, 9, 1, 5, 6]
l1.sort()  # Sorting the list in ascending order
print(l1, "\n")  # Output: [1, 2, 5, 5, 6, 9]

l2 = ["Banana", "Apple", "Cherry"]
l2.sort()  # Sorting the list of strings in alphabetical order ( Lowercase alphabets are larger than uppercase alphabets in ASCII value)
print(l2, "\n")  # Output: ['Banana', 'Cherry', 'Apple']

l2.sort(reverse=True)  # Sorting the list of strings in reverse alphabetical order
print(l2, "\n")  # Output: ['Cherry', 'Banana', 'Apple']

# Reversing a list
l1.reverse()  # Reversing the order of elements in the list
print(l1, "\n")  # Output: [9, 6, 5, 5, 2, 1]
# You can also use print(l1[::-1]) to reverse the list without modifying the original list

# Finding the index of an element
index_of_aakash = friends.index("Aakash")  # Finding the index of 'Aakash'
print(index_of_aakash, "\n")  # Output: 5 (index of 'Aakash')

# Counting occurrences of an element
count_of_five = friends.count(5)  # Counting how many times '5' appears in the list
print(count_of_five, "\n")  # Output: 1 (since '5' appears once in the list)

# Length of a list
length_of_friends = len(friends)  # Getting the number of elements in the list
print(length_of_friends, "\n")  # Output: 7 (number of elements in the list

# Copying a list

# Shallow copy means that if you modify the original list, the copy will also change
# Deep copy means that if you modify the original list, the copy will not change

# Shallow copy (just a reference, not a real copy)
print("original list:", friends, "\n")
shallow_copy = friends
shallow_copy[0] = "Pineapple"
print("After modifying shallow_copy:\n")
print("original list:", friends)         # friends is also changed
print("shallow_copy:", shallow_copy, "\n")

# Deep copy (creates a new list)
print(friends, "\n")
deep_copy = friends.copy()
deep_copy[1] = "Strawberry"
print("After modifying deep_copy:\n")
print("original list:", friends)         # friends is not changed
print("deep_copy:", deep_copy, "\n")

# Stacking lists
# Stacking lists means combining multiple lists into one
list1 = [1, 2, 3]
list2 = [4, 5, 6]
stacked_list = list1 + list2  # Combining list1 and list2
print(stacked_list, "\n")  # Output: [1, 2, 3, 4, 5, 6]

# Popping elements from a list
# Popping removes the last element from the list and returns it

# Difference between pop() and remove():
# - pop() removes an element at a specific index (default is the last element) and returns it
# - remove() removes the first occurrence of a specified value from the list and returns nothing

print(friends, "\n") # Output: ['Pineapple', 'Banana', 5, 345.06, False, 'Aakash', 'Rohan', 'Mango']
popped_element = friends.pop()  # Removes and returns the last element
print(popped_element, "\n")  # Output: Mango (the last element)
print(friends, "\n") # Output: ['Pineapple', 'Banana', 5, 345.06, False, 'Aakash', 'Rohan']

popped_element_at_index_2 = friends.pop(2)  # Removes and returns the element at index 2
print(popped_element_at_index_2)  # Output: 5 (the element at index 2)
print(friends, "\n")  # Output: ['Pineapple', 'Banana', 345.06, False, 'Aakash', 'Rohan']

# List Comprehensions -> provide a concise way to create lists based on existing lists
squared_numbers = [x**2 for x in range(10)]  # Squaring numbers from 0 to 9
print(squared_numbers, "\n")  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Filtering elements in a list using list comprehensions
even_numbers = [x for x in range(20) if x % 2 == 0]  # Getting even numbers from 0 to 19
print(even_numbers, "\n")  # Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Sum these even numbers -> sum of list items
Sum = sum(even_numbers)  # Summing the even numbers
print(Sum, "\n")  # Output: 90 (sum of even numbers from 0 to 18)

# Nested Lists
# Lists can contain other lists, creating a nested structure
nested_list = [[11, 21, 31], [4, 5, 6], [7, 8, 9]]
print(nested_list, "\n")  # Output: [[11, 21, 31], [4, 5, 6], [7, 8, 9]]
print(nested_list[0], "\n")  # Output: [11, 21, 31] (first inner list)
print(nested_list[1][1], "\n")  # Output: 5 (element at index 1 of the second inner list)

# List unpacking - assigning list elements to variables
a, b, c = [1, 2, 3]  # Unpacking
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3
print()

# List unpacking with nested lists
x, (y, z) = [1, [2, 3]]
print(x)  # Output: 1
print(y)  # Output: 2
print(z)  # Output: 3
print()