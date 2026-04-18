'''
> Date Created: 19/07/2025
> Author: Ishaan Rastogi
> Purpose: To show different types of loops in Python.
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

# For Loop - for iterating over a range of numbers
# for i in range( start, end, step ):
# If we don't specify start, it defaults to 0 and if we don't specify step, it defaults to 1

# For loop with range function
for i in range(1, 11, 2):  # This will print odd numbers from 1 to 10
    print(f"Current number: {i}")
print()

# While Loop - for iterating until a condition is met
# while (condition):

i = 1 # Initializing i
while (i <= 10):
    print(i)
    i += 2  # Increment by 2 to get odd numbers
print()

l = [ 1, "Harry", 3.14, True, None ]

# Iterate over a list using a while loop
i = 0  # Initializing index
while (i < len(l)):
    print(l[i])
    i += 1
print()

# Iterate over a list using a for loop
# For loop for lists
for i in l:
    print(i)
print()

# For loop for tuples
t = ( 1, "Harry", 3.14, True, None )
for i in t:
    print(i)
print()

# For loop for strings
s = "Harry"
for i in s:
    print(i)
print()

# For loop for dictionaries
d = { "name": "Harry", "age": 20, "is_student": True }
for key, value in d.items():
    print(f"{key}: {value}")
print()

# For loop for sets
st = { 1, "Harry", 3.14, True, None }
for i in st:
    print(i)
print()

# For Loop with else - to execute something when the loop completes normally using else
l = [1, 2, 3, 4, 5]
for i in l:
    print(i)
else:
    print("Loop completed successfully!")
print()

# While Loop with else - to execute something when the loop completes normally using else
i = 1
while (i <= 5):
    print(i)
    i += 1
else:
    print("While loop completed successfully!")
print()