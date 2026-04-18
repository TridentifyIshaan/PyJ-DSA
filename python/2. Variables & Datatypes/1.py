'''
> Date Created: 11/07/2025
> Author: Ishaan Rastogi
> Purpose: To print variables of different datatypes and operations on them
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

a = 1 #integer
b = 21.33 #float
c = "Ishaan" #string
d = False #boolean
e = None #NoneType -> To mark nothing

print(a, b, c, d, e) #Printing multiple variables

'''
    #Rules for naming variables:
    1. Variable names can only contain letters, numbers, and underscores. ( White spaces and other special characters are not allowed )
    2. Variable names cannot start with a number.
    3. Variable names are case-sensitive (e.g., `myVar` and `myvar` are different).
    4. Variable names cannot be a Python keyword (e.g., `if`, `for`, `while`, etc.).
    5. Variable names should be descriptive and meaningful to improve code readability.
'''

# Performing operations on variables

# Arithmetic operations
print (a + b) # Addition operation
print (a - b) # Subtraction operation
print (a * b) # Multiplication operation
print (a / b) # Division operation with float result
print (a % b) # Modulus operation with remainder
print (a ** b) # Exponentiation operation
print (a // b) # Floor division operation with integer result, round down to the nearest integer

# Assignment operations

a = 5 # Assigning a new value to a
a += 2 # Increment a by 2 and then assign the result back to a
print(a) # Print updated value of a
b -= 1.33 # Decrement b by 1.33
print(b) # Print updated value of b
c *= 2 # Repeat string c twice
print(c) # Print updated value of c
a /= 2 # Divide a by 2 and assign the result back to a
print(a) # Print updated value of a

# Comparison operations - Boolean results
print(a == b) # Check if a is equal to b
print(a != b) # Check if a is not equal to b
print(a > b) # Check if a is greater than b
print(a < b) # Check if a is less than b
print(a >= b) # Check if a is greater than or equal to b
print(a <= b) # Check if a is less than or equal to b

# Logical operations - Boolean results
print(a > 0 and b > 0) # Check if both a and b are greater than 0
print(a > 0 or b < 0) # Check if either a is greater than 0 or b is less than 0
print(not (a > 0)) # Check if a is not greater than 0

e = True or False
print(e) # Print the result of logical operation