'''
> Date Created: 16/08/2025
> Author: Ishaan Rastogi
> Purpose: To show how to use inheritance in Python
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

class Employee:

    company = "ITC"

    def show(self):
        print(f"Name: {self.name}, Language: {self.language}, Salary: {self.salary}")

class Programmer(Employee): # Whatever is there in the Employee class, it will be inherited by the Programmer class.
    company = "ITC Infotech"

    def showLanguage(self):
        print(f"The name is {self.name} and he is good at {self.language} language.")

a = Employee()
b = Programmer()

print(a.company, b.company)

# Base or parent class is Employee. Derived or child class is Programmer.
# This is a single inheritance, where one class inherits from another class.

'''
Terminal - Ctrl + Shift + `
> python "path to the file"
'''