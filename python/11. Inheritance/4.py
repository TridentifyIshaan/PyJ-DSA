'''
> Date Created: 17/08/2025
> Author: Ishaan Rastogi
> Purpose: To show how to use multilevel inheritance in Python
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

class Employee:
    a = 1

class Programmer(Employee): # Inherits Employee's properties
    b = 2

class Manager(Programmer): # Inherits Programmer's and Employee's properties
    c = 3

o = Manager()

print(o.a)  # Output: 1
print(o.b)  # Output: 2
print(o.c)  # Output: 3

# Multilevel inheritance is a type of inheritance where a class inherits from another class, which in turn inherits from another class. In this case, the Programmer class inherits from both Employee and Coder classes.

'''
Terminal - Ctrl + Shift + `
> python "path to the file"
'''