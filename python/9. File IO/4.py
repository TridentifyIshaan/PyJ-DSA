'''
> Date Created: 31/07/2025
> Author: Ishaan Rastogi
> Purpose: To read a file and print its content line by line.
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

# Since we are using a relative path here, use r before the string to avoid escape sequence issues
f = open(r"Code With Harry\9. File IO\file.txt") # By default, the file is opened in read mode
line = f.readline()
while ( line != ""):
    print(line, end='')  # Print the line without adding an extra newline
    line = f.readline()  # Read the next line
f.close()  # Close the file to free up resources

'''
Terminal - Ctrl + Shift + `
> python "path to the file"
'''