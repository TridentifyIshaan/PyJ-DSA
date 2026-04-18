'''
> Date Created: 25/07/2025
> Author: Ishaan Rastogi
> Purpose: To check if a string is palindrome using recursion.
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

def is_palindrome(s):
    s = s.lower()  # Convert the string to lowercase for case-insensitive comparison
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return is_palindrome(s[1:-1])  # Check the substring excluding the first and last characters

# User input for palindrome check
s = input("Enter a string to check if it is a palindrome: ")
print(f"Is the string '{s}' a palindrome? {is_palindrome(s)}")  # Output the result of the is_palindrome function
print()

'''

Terminal - Ctrl + Shift + `
> python "path to the file"

'''