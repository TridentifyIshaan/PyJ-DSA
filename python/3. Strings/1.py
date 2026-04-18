'''
> Date Created: 11/07/2025
> Author: Ishaan Rastogi
> Purpose: To show string operations and methods
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

# String is immutable, meaning it cannot be changed after creation

name = "Ishaan"

name_short = name[0:3]  # Slicing the string from 0 till 2
print(name_short)  # Output: Ish 

name_reverse = name[::-1]  # Reversing the string
print(name_reverse)  # Output: naahsI

# [start:end:step] -> if start is empty, it starts from the beginning, if end is empty, it goes till the end.

word = "Python"
print(word[1::2])  # Output: yhn

# String methods

print(len(name))  # Output: 6 (length of the string)
print(name.endswith("aan"))  # Checks if the string ends with "aan"
print(name.startswith("Ish"))  # Checks if the string starts with "Ish"
print(name.capitalize())  # Capitalizes the first letter of the string
print(name.upper())  # Converts the string to uppercase
print(name.lower())  # Converts the string to lowercase
print(name.replace("I", "A"))  # Replaces "I" with "A" in the string
print(name.find("s"))  # Finds the index of "s"
print(name.index("s"))  # Similar to find, but raises an error if not found
print(name.isalpha())  # Checks if the string contains only alphabetic characters
print(name.isalnum())  # Checks if the string contains only alphanumeric characters
print(name.isdigit())  # Checks if the string contains only digits
print(name.isspace()) # Checks if the string contains only whitespace
print(name.islower())  # Checks if the string is in lowercase
print(name.isupper())  # Checks if the string is in uppercase
print(name.split("s"))  # Splits the string at "s" and returns a list
print(name.strip())  # Removes leading and trailing whitespace (if any)
print(name.strip("I"))  # Removes leading and trailing "I" characters
print(name.lstrip())  # Removes leading whitespace
print(name.rstrip())  # Removes trailing whitespace
print(name.count("a"))  # Counts occurrences of "a" in the string
print(name.center(20, " "))  # Centers the string in a field of width
print(name.ljust(20, " "))  # Left-justifies the string in a field of width
print(name.rjust(20, " "))  # Right-justifies the string in a field of width
print(name.zfill(10))  # Pads the string with zeros on the left to make it 10 characters long
print(name.swapcase())  # Swaps the case of each character in the string
print(name.title())  # Converts the first character of each word to uppercase and the rest to lowercase
print(name.partition("a"))  # Splits the string at the first occurrence of "a" and returns a tuple
print(name.rpartition("a"))  # Splits the string at the last occurrence of "a" and returns a tuple
print(name.removeprefix("I"))  # Removes the prefix "I" from the string if it exists
print(name.removesuffix("aan"))  # Removes the suffix "aan" from the string if it exists
print(name.casefold())  # Converts the string to a case-insensitive format
print(name.join(["Hello ", " Welcome!"]))  # Joins the list with the string as a separator