'''
> Date Created: 16/08/2025
> Author: Ishaan Rastogi
> Purpose: To show why we need inheritance in Python
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

class Employee:

    company = "ITC"

    def show(self):
        print(f"Name: {self.name}, Language: {self.language}, Salary: {self.salary}")

class Programmer:
    company = "ITC Infotech"
    def show(self):
        print(f"Name: {self.name}, Language: {self.language}, Salary: {self.salary}")

    def showLanguage(self):
        print(f"The name is {self.name} and he is good at {self.language} language.")

a = Employee()
b = Programmer()

print(a.company, b.company)

# Here, we have two classes Employee and Programmer.
# Both classes have a method called show, but they are different methods but they are doing the same thing.
# This is why we need inheritance in Python, so that we can reuse the code and avoid duplication.
# Inheritance allows us to create a new class that inherits the properties and methods of an existing class.
# In this case, we can create a new class that inherits from Employee and Programmer and reuse the code.

# Code in next file will show how to use inheritance in Python.

'''
Terminal - Ctrl + Shift + `
> python "path to the file"
'''