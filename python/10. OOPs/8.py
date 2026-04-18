'''
> Date Created: 14/08/2025
> Author: Ishaan Rastogi
> Purpose: Creat a Class "Calculator" capable of finding square, cube and square root of a number.
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

class Calculator:
    def __init__(self, number):
        self.number = number

    def square(self):
        return self.number ** 2

    def cube(self):
        return self.number ** 3

    def square_root(self):
        return self.number ** 0.5
    
    @staticmethod
    def greet():
        return "Thank you for using the Calculator!"
    
n = int(input("Enter a number to perform operations: "))
c = Calculator(n)

print()
print(f"Square: {c.square()}")
print(f"Cube: {c.cube()}")
print(f"Square Root: {c.square_root()}")

print()
print(c.greet())

'''
Terminal - Ctrl + Shift + `
> python "path to the file"
'''