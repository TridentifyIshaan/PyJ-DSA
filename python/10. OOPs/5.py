'''
> Date Created: 14/08/2025
> Author: Ishaan Rastogi
> Purpose: To show the concept of constructors in Python Classes
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

# Class
class Employee:
    name = "Ishaan Rastogi"
    language = "Python"
    salary = 2000000

    # INITIALIZER / CONSTRUCTOR
    def __init__(self): # Dunder method
        print("Constructor called, Object Created")
    '''
    1. This is a special type of method called dunder methods.
    2. Dunder methods are methods that start and end with double underscores. They are also known as magic methods.
    3. They are used to implement the behavior of our objects in Python. For example, we can use dunder methods to define how our objects should be printed, how they should be compared, and how they should be added.
    4. This special INIT dunder get automatically called when we create an instance but not all dunder methods.
    '''
Ishaan = Employee("Ishaan Rastogi", "Java", 2500000)  # Object Creation / Instantiation
print(f"Name: {Ishaan.name}, Language: {Ishaan.language}, Salary: {Ishaan.salary}")

# TypeError: Employee.__init__() takes 1 positional argument but 4 were given
# Solution in next file

'''
Terminal - Ctrl + Shift + `
> python "path to the file"
'''