'''
> Date Created: 17/08/2025
> Author: Ishaan Rastogi
> Purpose: To show why we need super method in Python
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

# super() is a built-in function in Python used to access methods from a parent class.

class Employee:
    def __init__(self):
        print("Employee's __init__ called")
    a = 1

class Programmer(Employee): # Inherits Employee's properties
    def __init__(self):
        print("Programmer's __init__ called")
    b = 2

class Manager(Programmer): # Inherits Programmer's and Employee's properties
    def __init__(self):
        print("Manager's __init__ called")
    c = 3

o = Manager()
print(o.a, o.b, o.c)

'''
The output is as follows:
    Manager's __init__ called
    1 2 3

But if we want to call the dynamic methods of the parent class, we can use super() method.
Code implementation in next file.
'''

'''
Terminal - Ctrl + Shift + `
> python "path to the file"
'''