'''
> Date Created: 25/07/2025
> Author: Ishaan Rastogi
> Purpose: To calculate sum of numbers from 1 to n using recursion.
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

def sum_recursive(n):
    if n <= 1:
        return n
    else:
        return n + sum_recursive(n - 1)
    
# User input for sum calculation
n = int(input("Enter a number to calculate the sum from 1 to n: "))
print(f"The sum of numbers from 1 to {n} is: {sum_recursive(n)}")  # Output the result of the sum function
print()

'''

Terminal - Ctrl + Shift + `
> python "path to the file"

'''