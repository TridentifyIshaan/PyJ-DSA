'''
> Date Created: 14/08/2025
> Author: Ishaan Rastogi
> Purpose: To show the correct way of implementing INIT constructor in Python Classes
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

# Class
class Employee:
    name = "Ishaan Rastogi"
    language = "Python"
    salary = 2000000

    # INITIALIZER / CONSTRUCTOR
    def __init__(self, name, language, salary): # Dunder method
        self.name = name
        self.language = language
        self.salary = salary
        print("Constructor called, Object Created")

Ishaan = Employee("Ishaan Rastogi", "Java", 2500000)  # Object Creation / Instantiation
print(f"Name: {Ishaan.name}, Language: {Ishaan.language}, Salary: {Ishaan.salary}")

# Dunder methods list in Python: https://docs.python.org/3/reference/datamodel.html#special-method-names

'''
Terminal - Ctrl + Shift + `
> python "path to the file"
'''