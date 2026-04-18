'''
> Date Created: 10/08/2025
> Author: Ishaan Rastogi
> Purpose: Write a program to make a copy of a text file poems. txt”
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

with open (r"I:\My Drive\CS 100\Py-Lang\Code With Harry\9. File IO\poems.txt", "r") as f:
    content = f.read()

with open (r"I:\My Drive\CS 100\Py-Lang\Code With Harry\9. File IO\poems_copy.txt", "w") as f:
    f.write(content)

'''
Terminal - Ctrl + Shift + `
> python "path to the file"
'''