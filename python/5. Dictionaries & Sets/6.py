'''
> Date Created: 18/07/2025
> Author: Ishaan Rastogi
> Purpose: To create a dictionary with user input.
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

d = {}

name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Long way
# d["name"] = name
# d["age"] = age

# Short way
d.update({name : age})

print(d)

# If you update a key that already exists, it will overwrite the value.