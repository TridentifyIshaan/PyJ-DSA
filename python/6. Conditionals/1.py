'''
> Date Created: 18/07/2025
> Author: Ishaan Rastogi
> Purpose: To demonstrate the use of conditionals in Python.
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

# if elif else ladder - You can use if independently, but not elif or else without if.
# You can use elif without else.
# There can be multiple elif statements, but only one else statement.

a = int(input("Enter your age: "))
if ( a>18 ):
    print("You are an adult")
elif ( 0<a<18 ):
    print("You are a minor")
else:
    print("Invalid age, enter a valid age!\n")
print()

# Recursion is the process of calling a function from within itself. Let's try it to run it when someone enters an invalid age.
def check_age():
    a = int(input("Enter your age: "))
    if ( a>18 ):
        print("You are an adult")
    elif ( 0<a<18 ):
        print("You are a minor")
    else:
        print("Invalid age, enter a valid age!\n")
        check_age() # Recursion call to check_age function
    print()
check_age()