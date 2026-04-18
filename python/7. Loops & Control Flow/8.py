'''
> Date Created: 20/07/2025
> Author: Ishaan Rastogi
> Purpose: To print factorial of a number using loops
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

n = int(input("Enter a number to find its factorial: "))
factorial = 1
for i in range(2, n + 1):
    factorial *= i
print(f"The factorial of {n} is {factorial}")