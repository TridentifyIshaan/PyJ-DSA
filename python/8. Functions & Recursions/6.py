'''
> Date Created: 25/07/2025
> Author: Ishaan Rastogi
> Purpose: To calculate the Fibonacci sequence using recursion.
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

# Note: Recursive functions can be less efficient than iterative solutions for large inputs due to the overhead of function calls and stack memory usage.

# The Fibonacci sequence
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# User input for Fibonacci calculation
n = int(input("Enter a number to calculate the Fibonacci sequence: "))
print(f"The {n}th number in the Fibonacci sequence is: {fibonacci(n)}")  # Output the result of the Fibonacci function
print()
# Note: Recursive functions can be less efficient for large inputs, especially in the case of Fibonacci, due to repeated calculations.

'''

Terminal - Ctrl + Shift + `
> python "path to the file"

'''