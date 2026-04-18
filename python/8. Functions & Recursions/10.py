'''
> Date Created: 25/07/2025
> Author: Ishaan Rastogi
> Purpose: To find power of a number using recursion.
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

def power(base, exp):
    if exp == 0:
        return 1
    elif exp < 0:
        return 1 / power(base, -exp)
    else:
        return base * power(base, exp - 1)
    
# User input for power calculation
base = float(input("Enter the base number: "))
exp = int(input("Enter the exponent: "))
print(f"{base} raised to the power of {exp} is: {power(base, exp)}")  # Output the result of the power function
print()

'''

Terminal - Ctrl + Shift + `
> python "path to the file"

'''