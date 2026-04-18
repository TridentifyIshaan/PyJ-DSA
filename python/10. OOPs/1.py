'''
> Date Created: 12/08/2025
> Author: Ishaan Rastogi
> Purpose: To show concept of class and object in Python
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

# Class
class Employee:
    name = "Ishaan Rastogi"
    language = "Python"
    salary = 2000000

# Object Creation / Instantiation
Ishaan = Employee()

# Calling the attributes of the class
print(Ishaan.name, Ishaan.language, Ishaan.salary)

Ishaan2 = Employee()
Ishaan2.language = "Java" # Changing the language of Ishaan2 object
print(Ishaan2.name, Ishaan2.language, Ishaan2.salary)

# Here name and salary are class attributes, they are same for all objects of the class.
# Here language is an instance/object attribute, it can be different for each object of the class.

# As you can see here, instance attribute take preference over class attributes during assignment and retrieval.

'''
Terminal - Ctrl + Shift + `
> python "path to the file"
'''