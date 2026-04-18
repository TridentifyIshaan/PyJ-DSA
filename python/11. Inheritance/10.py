'''
> Date Created: 17/08/2025
> Author: Ishaan Rastogi
> Purpose: To show how to implement property decorators and setter in Python
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

class Employee:

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self, value):
        self.fname = value.split()[0]
        self.lname = value.split()[1]

e = Employee()
e.name = "Ishaan Rastogi"
print(e.name)
print(e.fname, e.lname)

# property decorators allow you to define methods that can be accessed like attributes.
# This allows you to control access to the attributes and perform validation or transformation when getting or setting them.

# setter is used to define a method that is called when the attribute is set.
# This allows you to perform validation or transformation when setting the attribute.

'''
Terminal - Ctrl + Shift + `
> python "path to the file"
'''