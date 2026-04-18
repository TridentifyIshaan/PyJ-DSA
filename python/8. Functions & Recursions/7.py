'''
> Date Created: 25/07/2025
> Author: Ishaan Rastogi
> Purpose: To reverse a string using recursion.
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])
    
# User input for string reversal
s = input("Enter a string to reverse it: ")
print(f"The reversed string is: {reverse_string(s)}")  # Output the result of the reverse_string function
print()

'''

Terminal - Ctrl + Shift + `
> python "path to the file"

'''