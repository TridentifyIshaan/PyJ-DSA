'''
> Date Created: 17/08/2025
> Author: Ishaan Rastogi
> Purpose: To show why we need class method in Python
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

# class method is a method that is bound to the class and not the instance of the class.
# @classmethod is a decorator that is used to define a class method.
# It takes the class as the first argument and can be called on the class itself or on an instance of the class.

class Employee:
    a = 1
    def show(self):
        print(f"The class attribrute of a is {self.a}")

e = Employee()
e.a = 45
e.show() #output will be 45, because it is an instance variable. But we want 1 as an answer. To get so, next file.

'''
Terminal - Ctrl + Shift + `
> python "path to the file"
'''