'''
> Date Created: 25/07/2025
> Author: Ishaan Rastogi
> Purpose: To find greatest number out of three numbers.
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

def greatest(a, b,c ):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    
# User input for greatest number calculation
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
print(f"The greatest number is: {greatest(a, b, c)}")  # Output the result of the greatest function
print()

'''

Terminal - Ctrl + Shift + `
> python "path to the file"

'''