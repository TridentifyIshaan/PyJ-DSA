'''
> Date Created: 31/07/2025
> Author: Ishaan Rastogi
> Purpose: To showcase the best practice to open files
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

# To leave the hassle of closing the file manually, we can use the with statement to open the file which automatically closes the file after the block of code is executed.
with open(r"Code With Harry\9. File IO\file2.txt", "a") as f:
    st = "\nThis is the sixth line.\nThis is the seventh line."
    f.write(st)

'''
Terminal - Ctrl + Shift + `
> python "path to the file"
'''
