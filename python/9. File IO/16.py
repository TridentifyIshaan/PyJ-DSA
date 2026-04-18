'''
> Date Created: 10/08/2025
> Author: Ishaan Rastogi
> Purpose: Write a python program to rename a file to "new.txt".
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

# Approach - Make copy of a file and rename it to "new.txt" and delete the original file.

with open (r"I:\My Drive\CS 100\Py-Lang\Code With Harry\9. File IO\poems_copy.txt", "r") as f:
    content = f.read()

with open (r"I:\My Drive\CS 100\Py-Lang\Code With Harry\9. File IO\new.txt", "w") as f:
    f.write(content)

import os # Operating System module
os.remove(r"I:\My Drive\CS 100\Py-Lang\Code With Harry\9. File IO\poems_copy.txt")

'''
Terminal - Ctrl + Shift + `
> python "path to the file"
'''
