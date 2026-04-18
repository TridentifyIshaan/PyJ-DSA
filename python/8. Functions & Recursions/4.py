'''
> Date Created: 31/07/2025
> Author: Ishaan Rastogi
> Purpose: To print the following pattern using recursion:
***
**
* for n = 3
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

def pattern(n):
    if n == 0:
        return # Empty return means stop and leave, nothing will be printed and conditional will break
    print ("*" * n)  # Print n stars
    pattern(n-1)

n = int(input("Enter the number of lines for the pattern: "))  # User input for number of lines
pattern(n)  # Call the pattern function with user input

'''

Terminal - Ctrl + Shift + `
> python "path to the file"

'''