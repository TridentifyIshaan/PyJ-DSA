'''
> Date Created: 14/08/2025
> Author: Ishaan Rastogi
> Purpose: To show concept of self parameter in Python Classes
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

# Self Parameter - Self reference to the instance of the class itself. It is used to access variables that belong to the class. It is automatically passed with a method call from an object.

# Class
class Employee:
    name = "Ishaan Rastogi"
    language = "Python"
    salary = 2000000

    # Method
    def getInfo():
        print(f"Name: {Employee.name}, Language: {Employee.language}, Salary: {Employee.salary}")

Ishaan = Employee()  # Object Creation / Instantiation
Ishaan.language = "Java"  # Changing the language of Ishaan object
'''
Ishaan.getInfo()  # Calling the method to get info of Ishaan object
-> TypeError: Employee.getInfo() takes 0 positional arguments but 1 was given

What happens is Ishaan.getInfo() gets converted to Employee.getInfo(Ishaan) automatically which states we have given 1 positional argument (Ishaan) but the method is defined to take 0 positional arguments.

To fix this, we need to add the self parameter which we will cover in the next file.
'''

'''
Terminal - Ctrl + Shift + `
> python "path to the file"
'''