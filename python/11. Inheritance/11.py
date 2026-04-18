'''
> Date Created: 17/08/2025
> Author: Ishaan Rastogi
> Purpose: To show concept of operator overloading in Python
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

# Operator overloading allows you to define how operators behave for user-defined classes.
# This is done using dunder methods (also known as magic methods) that start and end with double underscores.

class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n

n = Number(1)
m = Number(2)

print (n + m)  # This will raise an error because + is not defined for Number class until we define it using __add__ method.


'''
Similarly we can define other operators:
a + b # a.__add__(b)
a - b # a.__sub__(b)
a * b # a.__mul__(b)
a / b # a.__truediv__(b)
a // b # a.__floordiv__(b)
a % b # a.__mod__(b)
a ** b # a.__pow__(b)
a == b # a.__eq__(b)
a != b # a.__ne__(b)
a < b # a.__lt__(b)
a <= b # a.__le__(b)
a > b # a.__gt__(b)
# a >= b # a.__ge__(b)

Other dunder methods can be used to define how the object behaves in different contexts, such as:
# a.__str__() for string representation
# a.__len__() for length

'''

'''
Terminal - Ctrl + Shift + `
> python "path to the file"
'''