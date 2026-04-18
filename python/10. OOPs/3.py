'''
> Date Created: 14/08/2025
> Author: Ishaan Rastogi
> Purpose: To show right way of implementing self parameter in Python Classes
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
    def getInfo(self):
        print(f"Name: {self.name}, Language: {self.language}, Salary: {self.salary}")
    # Self parameter is used to access the instance variables of the class. It refers to the object itself which is calling the method. Here, object is Ishaan and self refers to Ishaan object.

    def greet(self):
        print(f"Hello {self.name}, Welcome to the Python Class!")

Ishaan = Employee()  # Object Creation / Instantiation
Ishaan.language = "Java"  # Changing the language of Ishaan object

Ishaan.getInfo()  # Hence no conversion to Employee.getInfo(Ishaan) happens.

# Moral of the story: Always use self parameter in methods of a class to refer to the instance variables of the class. You have to give a self parameter in the method defination, , whether you use it or not, but you don't have to pass it while calling the method. Python does it automatically.

Ishaan.greet()  # Calling the greet method of Ishaan object

# NOTE - Self is not a keyword in Python, it is just a convention. You can use any other name instead of self, but it is highly recommended to use self for better readability and understanding of the code.

'''
Terminal - Ctrl + Shift + `
> python "path to the file"
'''