'''
> Date Created: 16/08/2025
> Author: Ishaan Rastogi
> Purpose: To show how to use multiple inheritance in Python
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

class Employee:

    company = "ITC"
    name = "Ishaan Rastogi"
    salary = 50000

    def show(self):
        print(f"Name: {self.name}, Language: {self.language}, Salary: {self.salary}")

class Coder:
    language = "Python"

    def printLanguages(self):
        print(f"Out of all the languages, you are best at {self.language} language.")

class Programmer(Employee, Coder): # Whatever is there in the Employee & Coder classes, it will be inherited by the Programmer class.
    company = "ITC Infotech"

    def showLanguage(self):
        print(f"He works at {self.company} and he is good at {self.language} language.")

a = Programmer()

a.show()
a.printLanguages()
a.showLanguage()

# Base or parent class is Employee. Derived or child class is Programmer.
# This is a multiple inheritance, where one class inherits from multiple classes.
# Here, Programmer inherits from both Employee and Coder classes.

'''
Terminal - Ctrl + Shift + `
> python "path to the file"
'''