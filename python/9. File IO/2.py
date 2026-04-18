'''
> Date Created: 31/07/2025
> Author: Ishaan Rastogi
> Purpose: To write to a file and read from it
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

f = open(r"Code With Harry\9. File IO\file2.txt", "w")
st = "Hello, this is a test file.\nThis is the second line.\nThis is the third line."
f.write(st)

f.close()

# if the file already exists, it will be overwritten

'''
Terminal - Ctrl + Shift + `
> python "path to the file"
'''
