'''
> Date Created: 17/08/2025
> Author: Ishaan Rastogi
> Purpose: To show how to implement class method in Python
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

# class method is a method that is bound to the class and not the instance of the class.
# @classmethod is a decorator that is used to define a class method.
# It takes the class as the first argument and can be called on the class itself or on an instance of the class.

class Employee:
    a = 1
    @classmethod # adding this decorator makes this method a class method
    def show(cls): # replacing self with cls, which is the convention for class methods
        print(f"The class attribrute of a is {cls.a}")

e = Employee()
e.a = 45
e.show()

'''
Terminal - Ctrl + Shift + `
> python "path to the file"
'''