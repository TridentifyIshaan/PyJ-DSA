'''
> Date Created: 31/07/2025
> Author: Ishaan Rastogi
> Purpose: To read a file and prints its lines.
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

# Since we are using a relative path here, use r before the string to avoid escape sequence issues
f = open(r"Code With Harry\9. File IO\file2.txt") # By default, the file is opened in read mode
line1 = f.readline()  # Read the first line of the file
line2 = f.readline()  # Read the second
line3 = f.readline()  # Read the third line
line4 = f.readline()  # Read the fourth line (if exists)
print(line1, end='')  # Print the first line without adding an extra newline
print(line2, end='')  # Print the second line without adding an extra newline
print(line3, end='')  # Print the third line without adding an extra newline
print(line4)  # Print the fourth line which is empty here

# To check if line4 is empty, you can use:
print(line4 =="") # This will print True if line4 is empty, otherwise False

f.close()  # Close the file to free up resources

'''
Terminal - Ctrl + Shift + `
> python "path to the file"
'''