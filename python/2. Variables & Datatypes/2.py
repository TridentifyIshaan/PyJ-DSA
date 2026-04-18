'''
> Date Created: 11/07/2025
> Author: Ishaan Rastogi
> Purpose: To show type function and its usage (typecasting)
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

a = 31
t = type(a) # class <int>
print(t)  # Prints the type of variable a

b = 21.33
t = type(b) # class <float>
print(t)  # Prints the type of variable b

# Typecasting
a = str(a)  # Convert integer a to string
t = type(a) # class <str>
print(t)  # Prints the type of variable a after typecasting

b = int(b)  # Convert float b to integer
t = type(b) # class <int>
print(t)  # Prints the type of variable b after typecasting

# str, float, int, bool, complex are typecasting functions in Python
c = 1 + 2j  # Complex number
print(c)
t = type(c) # class <complex>
print(t)  # Prints the type of variable c