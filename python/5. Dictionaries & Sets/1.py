'''
> Date Created: 17/07/2025
> Author: Ishaan Rastogi
> Purpose: To demonstrate the use of dictionaries in Python, including their properties, methods, and operations.
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

# Dictionaries in Python
# A dictionary is a collection of key-value pairs

# Non-homogeneous data structure
# It can contain different data types as values, but keys must be unique and immutable (strings, numbers, tuples) Eg- 100 is an integer but the list given below is a list

# It is mutable, unordered, and indexed.

marks = {
    "Ishaan" : 100,
    "Rishabh" : 90,
    "Rohan" : 80,
    "list" : [1, 2, 3, 4, 5],
    0 : "Harry"
}

print(marks, type(marks))
print()

# We can't change the key of a dictionary
# marks["Ishaan"] = 99 # This will not change the key, it will change the value
# print(marks)
# marks[0] = 99 # This will give an error because 0 is not a valid key

# Every key in a dictionary must be unique
# If we try to add a key that already exists, it will update the value
marks["Ishaan"] = 99
print(marks)
print()

# We can add a new key-value pair to the dictionary
marks["Aman"] = 85
print(marks)
print()

# Updating a value in the dictionary - Adds key-value pair if key does not exist, otherwise updates the value
marks.update({"Rishabh": 95, "Renuka": 100})
print(marks)
print()

# We can also delete a key-value pair from the dictionary
# NOTE - Only the key is deleted, not the value because only key is unique meaning 2 keys can have the same value also.

del marks["Rohan"]
print(marks)
print()

# We can check if a key exists in the dictionary
print("Ishaan" in marks)  # Returns True if key exists, otherwise False
print("Rohan" in marks)   # Returns False since Rohan was deleted
print()

# Very Important Difference between accessing values in a dictionary

# We can get the value of a key using the get() method
print(marks.get("Ishaan"))  # Returns 99
print(marks.get("Rohan"))   # Returns None since Rohan was deleted
# If accessing a key that does not exist, None is returned
print(marks.get("Hello"))
print()

# New way to access values in a dictionary
print(marks["Ishaan"]) # prints 99
print(marks["list"]) # prints [1, 2, 3, 4, 5]
# If accessing a key that does not exist, it will raise a KeyError
# print(marks["Hello"])  # Raises KeyError
print()

# We can also get all the keys and values of the dictionary
print(marks.keys())   # Returns a view object containing all the keys
print(marks.values()) # Returns a view object containing all the values
print(marks.items())  # Returns a view object containing all the key-value pairs
print()

# We can also iterate over the keys and values of the dictionary
for key in marks:
    print(key, ":", marks[key])  # Prints each key and its corresponding value
print()

# We can also use the items() method to iterate over the key-value pairs
for key, value in marks.items():
    print(key, ":", value)  # Prints each key and its corresponding value
print()

# We can also clear the dictionary
marks.clear()  # Removes all the key-value pairs from the dictionary
print(marks)  # Prints an empty dictionary - {}
print()

# We can also copy the dictionary

marks = {"Ishaan": 99, "Rishabh": 95, "Renuka": 100}

# Shallow copy - On change in original, the copy will also change if the mutable object is modified.
# Deep copy - On change in original, the copy will not change if the mutable object is modified.

marks = {"Ishaan": 99, "Rishabh": 95, "Renuka": 100, "scores": [10, 20, 30]}

marks_shallow = marks.copy()  # Shallow copy
import copy
marks_deep = copy.deepcopy(marks)  # Deep copy

# Modify the nested list in the original dictionary
marks["scores"].append(40)
marks["Rishabh"] = 98  # Update a value in the original dictionary
del marks["Rishabh"]

print("Original:", marks)
print("Shallow Copy:", marks_shallow)  # 'scores' list will also have 40 (reference copied)
print("Deep Copy:", marks_deep)        # 'scores' list will NOT have 40 (new list copied)
print()

# No change when we changed the original dictionary's value of Rishabh in deep or shallow copies and even when we deleted the key Rishabh in original dictionary, it did not affect the shallow or deep copies.

# Shallow or deep copies can be useful when the data is crucial and we want to keep a backup of the original data before making changes because if we make changes in the original data, it will not affect the copies if the object is immutable.

# Creating a new dictionary from a list of keys using fromkeys()
# fromkeys() can also be used to create a dictionary with default values
keys = ['a', 'b', 'c']
new_dict = dict.fromkeys(keys, 0)  # Creates a new dictionary with keys from the list and all values set to 0
print(new_dict)  # {'a': 0, 'b': 0, 'c': 0}
print()

keys = ['x', 'y', 'z']
new_dict = dict.fromkeys(keys)  # Creates a new dictionary with keys from the list and all values set to None
print(new_dict)  # {'x': None, 'y': None, 'z': None}
print()

# Combining two lists into a dictionary using zip()

# the zip() function can be used to combine two lists into a dictionary
# It pairs elements from the two lists together, creating key-value pairs in the dictionary
keys = ['name', 'age', 'city']
values = ['Alice', 30, 'New York']
combined_dict = dict(zip(keys, values))  # Creates a dictionary by pairing keys and values
print(combined_dict)  # {'name': 'Alice', 'age': 30, 'city': 'New York'}
print()

# Nested dictionaries
# We can also create dictionaries within dictionaries
nested_dict = {
    "student1": {"name": "Ishaan", "age": 20, "marks": 99},
    "student2": {"name": "Rishabh", "age": 21, "marks": 95},
    "student3": {"name": "Renuka", "age": 22, "marks": 100}
}
print(nested_dict)
print(nested_dict["student1"]["name"])  # Accessing nested dictionary values
print(nested_dict["student2"]["marks"])  # Accessing nested dictionary values
print()

# pop() method
# The pop() method removes a key-value pair from the dictionary and returns the value
popped_value = marks.pop("Renuka", "Key not found")
popped_2 = marks.pop("Rishabh", "Key not found")

# Removes the key and returns its value, or "Key not found" if the key does not exist
print(marks) # To check what the dictionary currently looks like
print(popped_value)  # Prints the value of the popped key
print(popped_2)  # Prints the value of the popped key
print(marks)  # Prints the dictionary after popping the key
print()

# popitem() method
# The popitem() method removes and returns the last inserted key-value pair as a tuple
last_item = marks.popitem()  # Removes the last inserted key-value pair and returns it
print(last_item)  # Prints the last inserted key-value pair as a tuple
print(marks)  # Prints the dictionary after popping the last item
print()

# setdefault() method
# The setdefault() method returns the value of a key if it exists, otherwise it sets the key with a default value and returns that value
default_data = marks.setdefault("NewKey", "DefaultValue")  # Sets "NewKey" with "DefaultValue" if it does not exist
print(default_data)  # Prints the value of the key, which is "DefaultValue" since "NewKey" did not exist
print(marks)  # Prints the dictionary after setting the default value
print()

# We can also use the setdefault() method to get the value of a key if it exists
existing_value = marks.setdefault("Ishaan", "NewDefaultValue")  # Returns the value of "Ishaan" if it exists, otherwise sets it to "NewDefaultValue"
print(existing_value)  # Prints the value of "Ishaan", which is 99
print(marks)  # Prints the dictionary after checking the existing key
print()

# How setdefault() even useful
# It can be useful when we want to ensure a key exists in the dictionary with a default value, especially when working with nested dictionaries or when we want to avoid KeyError exceptions.
# Example: Using setdefault() with nested dictionaries
nested_scores = {}
students = ["Ishaan", "Rishabh", "Renuka"]
subjects = ["Math", "Science"]

for i in students:
    for i in subjects:
        # Ensure each student has a dictionary for subjects
        nested_scores.setdefault(i, {})
        # Set a default score for each subject if not already present
        nested_scores[i].setdefault(i, 0)

print(nested_scores)
print()

# It can also be used to initialize a key with a default value if it does not exist, which can be helpful in scenarios where we want to accumulate values for a key over time.
# For example, if we want to count occurrences of items in a list, we can use setdefault() to initialize the count for each item if it does not exist in the dictionary.
# Example of using setdefault() to count occurrences of items in a list
items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
item_count = {}
for i in items:
    item_count.setdefault(i, 0)  # Initialize the count for the item if it does not exist
    item_count[i] += 1  # Increment the count for the item
print(item_count)  # Prints the count of each item in the list

# basically increasing value of the key if it exists, otherwise setting it to 0 and then increasing it by 1
print()

# Operations on dictionaries
# We can perform various operations on dictionaries, such as merging, comparing, and checking for equality

# Combining dictionaries using the union operator (Python 3.9+)
# We can combine two dictionaries using the union operator (|) in Python 3.9
dict_a = {"x": 1, "y": 2}
dict_b = {"y": 3, "z": 4}
combined_dict = dict_a | dict_b  # Combines dict_a and dict_b, with dict_b's values taking precedence for duplicate keys
# Note: This will not modify the original dictionaries
# It creates a new dictionary with the combined key-value pairs
print(dict_a)  # {'x': 1, 'y': 2}
print(dict_b)  # {'y': 3, 'z': 4}
print(combined_dict)  # {'x': 1, 'y': 3, 'z': 4}
print()

# Combining dictionaries using the union operator (|=) in Python 3.9
# We can also combine dictionaries using the union operator (|=) which modifies the first dictionary
dict_a |= dict_b  # Merges dict_b into dict_a, with dict_b's values taking precedence for duplicate keys
# Note: This modifies dict_a and does not create a new dictionary
print(dict_a)  # {'x': 1, 'y': 3, 'z': 4}
print(dict_b)  # {'y': 3, 'z': 4}
print()

# Merging dictionaries using the update() method
# We can also combine dictionaries using the update() method, which modifies the first dictionary in place
dict_a.update(dict_b)  # Updates dict_a with the key-value pairs from dict_b
# Note: This modifies dict_a and does not create a new dictionary
print(dict_a)  # Prints the merged dictionary - {'x': 1, 'y': 3, 'z': 4}
print(dict_b)  # The original dict_b remains unchanged - {'y': 3, 'z': 4}
print()

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 2, "c": 3}
dict3 = {"a": 1, "b": 2}

# Comparing dictionaries for equality
print(dict1 == dict2)  # Returns False since dict1 and dict2 are not equal
print(dict1 == dict3)  # Returns True since dict1 and dict3 are equal
print()

# Checking if a key exists in a dictionary
print("a" in dict1)  # Returns True since "a" is a key
print("d" in dict1)  # Returns False since "d" is not a key
print()

# Dictionary comprehensions
# We can create dictionaries using dictionary comprehensions, which is a concise way to create dictionaries from existing iterables
squared_dict = {x: x**2 for x in range(5)}  # Creates a dictionary with keys as numbers from 0 to 4 and values as their squares
print(squared_dict) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
print()

# Dictionary comprehensions with conditions
even_squared_dict = {x: x**2 for x in range(10) if x % 2 == 0}  # Creates a dictionary with keys as even numbers from 0 to 9 and values as their squares
print(even_squared_dict)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
print()