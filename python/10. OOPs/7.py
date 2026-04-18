'''
> Date Created: 14/08/2025
> Author: Ishaan Rastogi
> Purpose: Creat a Class "Programmer" for storing information of few programmers working at Microsoft.
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

class Programmer:
    company = "Microsoft" # Class variable since it is common for all instances

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("Ishaan Rastogi", 100000, 1234)
print(f"Name: {p.name}, Salary: {p.salary}, PIN: {p.pin}, Company: {p.company}")
r = Programmer("Rohan Sharma", 120000, 5678)
print(f"Name: {r.name}, Salary: {r.salary}, PIN: {r.pin}, Company: {r.company}")

'''
Terminal - Ctrl + Shift + `
> python "path to the file"
'''