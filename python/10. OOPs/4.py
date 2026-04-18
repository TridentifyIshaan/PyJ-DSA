'''
> Date Created: 14/08/2025
> Author: Ishaan Rastogi
> Purpose: To show the concept of static method in Python Classes
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

# Class
class Employee:
    name = "Ishaan Rastogi"

    # Static Method is a method that belongs to the class rather than any object instance. It does not require anything from instance.

    @staticmethod # Static Method tells the Python interpreter that this method doesn't require a self parameter.
    def greet():
        print(f"Hello {Employee.name}, Welcome to the Python Class!")

Ishaan = Employee()  # Object Creation / Instantiation
Ishaan.greet()  # Calling the greet method of Ishaan object

'''
Terminal - Ctrl + Shift + `
> python "path to the file"
'''