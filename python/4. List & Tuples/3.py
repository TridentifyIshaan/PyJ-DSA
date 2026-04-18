'''
> Date Created: 14/07/2025
> Author: Ishaan Rastogi
> Purpose: To create a list of fruits with user input
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

'''

Cumbersome way to create a list of fruits:

fruits = []

f1 = input("Enter fruit 1: ")
f2 = input("Enter fruit 2: ")
f3 = input("Enter fruit 3: ")
f4 = input("Enter fruit 4: ")
f5 = input("Enter fruit 5: ")
f6 = input("Enter fruit 6: ")
f7 = input("Enter fruit 7: ")
fruits.append(f1)
fruits.append(f2)
fruits.append(f3)
fruits.append(f4)
fruits.append(f5)
fruits.append(f6)
fruits.append(f7)

print(fruits)
'''

# Efficient way to create a list of fruits using list comprehension

# Using list comprehension to create a list of fruits & formatted input prompts
fruits = [input(f"Enter fruit {i+1}: ") for i in range(7)]
print(fruits)

fruits.sort()
print(fruits)  # Sorts the list of fruits in alphabetical order