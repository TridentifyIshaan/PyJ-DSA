'''
> Date Created: 14/08/2025
> Author: Ishaan Rastogi
> Purpose: Create a class with a class attribute a;create an object from it and set 'a' directly using 'object.a = o'. Does this change the class attribute?
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

class cls:
    a = 10

o = cls()

print(o.a) # Accessing class attribute because instance attribute 'a' does not exist yet

print(cls.a)  # Accessing class attribute through instance

o.a = 0 # This changes the instance attribute, not the class attribute

print(cls.a)  # Class attribute remains unchanged

print(o.a)    # Accessing instance attribute

'''
Terminal - Ctrl + Shift + `
> python "path to the file"
'''