'''
> Date Created: 25/07/2025
> Author: Ishaan Rastogi
> Purpose: To find GCD using recursion.
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

# greatest common divisor (GCD)
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# User input for GCD calculation
a = int(input("Enter the first number for GCD calculation: "))
b = int(input("Enter the second number for GCD calculation: "))
print(f"The GCD of {a} and {b} is: {gcd(a, b)}")  # Output the result of the GCD function
print()

'''

Terminal - Ctrl + Shift + `
> python "path to the file"

'''