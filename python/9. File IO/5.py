'''
> Date Created: 31/07/2025
> Author: Ishaan Rastogi
> Purpose: To not let a file be overwritten if it already exists
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

# Append mode is used to create a safety layer to prevent overwriting existing files as in write mode.
# I have personal experience of losing data due to overwriting files when I was learning Python for the first time in 11th grade.
# Therefore, I always use append mode when working with writing data into the files.

f = open(r"Code With Harry\9. File IO\file2.txt", "a") # Append means add at the end and here end means the end of the file.
st = "\nThis is the fourth line.\nThis is the fifth line."
f.write(st)
f.close()

# if the file already exists, it will be overwritten

'''
Terminal - Ctrl + Shift + `
> python "path to the file"
'''
