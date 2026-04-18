'''
> Date Created: 25/07/2025
> Author: Ishaan Rastogi
> Purpose: To know about functions in Python
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

'''
A. Function is a block of code that only runs when it is called. It is used to perform a specific task and can be reused multiple times in a program.

B. Function definition is done using the `def` keyword followed by the function name and (). The code block within every function starts with a colon(:) and is indented.

C. Function call is the process of executing the function. It is done by writing the function name followed by ().

D. Types of functions:
    1. Built-in functions: These are functions that are already defined in Python, such as `print()`, `len()`, etc.
    2. User-defined functions: These are functions that are defined by the user to perform specific tasks.

        i) In user-defined functions, we can pass parameters to the function. Parameters are variables that are passed to the function when it is called. They allow us to pass data into the function.

        ii) Arguments are the actual values that are passed to the function when it is called. They are used to provide input to the function.
'''

def greet(name, ending): # name & ending are the parameters
    print(f"Hello, {name}! {ending}")

# Function call with an argument
greet("Ishaan", "Welcome to the world of Python functions.") # These are the arguments passed to the function greet
greet("Divya", "Hope you are enjoying learning Python!") # Another function call with different arguments
print()

# returning a value from a function
def add(a, b):
    return a + b  # This function returns the sum of a and b

result = add(7,3)  # Function call with arguments 7 and 3
print(f"The sum of 7 and 3 is: {result}")  # Output the result of the function call
print()

# Function with default parameters
# Default parameters allow us to define a function with default values for parameters, which can be overridden when the function is called.

def greet(name = "Ishaan"):
    gr = f"Hello, {name}"
    print(gr)

greet()
greet("Divya")
print()

# Function with variable-length arguments
# Variable-length arguments allow us to pass a variable number of arguments to a function. This is done using the *args syntax.

# *args allows us to pass a variable number of positional arguments to a function.

def numbers(*args):
    for num in args:
        print(num)

numbers(1, 2, 3, 4, 5)
print()

'''
Recursive functions
A recursive function is a function that calls itself to solve a problem. It is used to solve problems that can be broken down into smaller subproblems.

Eg - factorial(n) = n * factorial(n-1)
1! = 1
2! = 2 * 1! = 2
3! = 3 * 2! = 6
4! = 4 * 3! = 24
'''

def factorial(n):
    if (n == 0 or n == 1):
        return 1
    elif n < 0:
        return n * factorial(n-1)
    else:
        return "Invalid input, please enter a non-negative integer."

# User input for factorial calculation
n = int(input("Enter a number to calculate its factorial: "))
print(f"The factorial of {n} is: {factorial(n)}")  # Output the result of the factorial function
print()

# Note: Recursive functions can lead to infinite recursion if not handled properly, so it's important to have a base case to stop the recursion.

'''

Terminal - Ctrl + Shift + `
> python "path to the file"

'''