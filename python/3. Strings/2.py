'''
> Date Created: 11/07/2025
> Author: Ishaan Rastogi
> Purpose: To show string formatting and escape sequence characters
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

# String formatting
age = 20
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)  # Output: My name is Ishaan and I am 20

# Escape sequence characters

print("Hello\nWorld")  # New line
print("\n")
print("Hello\tWorld")  # Tab space
print("\n")
print("Hello\\World")  # Backslash
print("\n")
print("Hello\"World\"")  # Double quotes
print("\n")
print('Hello\'World\'')  # Single quotes
print("\n")
print("Hello\bWorld")  # Backspace - removes the last character
print("\n")
print("Hello\fWorld")  # Form feed - moves the cursor to the next line
print("\n")
print("Hello\rWorld")  # Carriage return - moves the cursor to the beginning of the line
print("\n")
print("Hello\vWorld")  # Vertical tab - moves the cursor down to the next line
print("\n")
print("Hello\0World")  # Null character (not visible)
print("\n")
print("World \x48\x65\x6c\x6c\x6f")  # Hexadecimal escape sequence for "Hello"