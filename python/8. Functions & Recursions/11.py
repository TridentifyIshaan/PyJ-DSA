'''
> Date Created: 25/07/2025
> Author: Ishaan Rastogi
> Purpose: To find the length of a string using recursion.
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

def string_length(s):
    if s == "":
        return 0
    else:
        return 1 + string_length(s[1:])  # Count the first character and recurse on the rest of the string
    
# User input for string length calculation
s = input("Enter a string to find its length: ")
print(f"The length of the string '{s}' is: {string_length(s)}")  # Output the result of the string_length function
print()

'''

Terminal - Ctrl + Shift + `
> python "path to the file"

'''