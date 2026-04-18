'''
> Date Created: 31/07/2025
> Author: Ishaan Rastogi
> Purpose: To read a file and print its content.
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

# Since we are using a relative path here, use r before the string to avoid escape sequence issues
f = open(r"Code With Harry\9. File IO\file.txt") # By default, the file is opened in read mode
data = f.read()  # Read the entire content of the file
print(data)  # Print the content of the file
f.close()  # Close the file to free up resources

# f is file object or file pointer, which is a variable that points to the file object in memory.

'''
Terminal - Ctrl + Shift + `
> python "path to the file"
'''