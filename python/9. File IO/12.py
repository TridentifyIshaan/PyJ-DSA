'''
> Date Created: 03/08/2025
> Author: Ishaan Rastogi
> Purpose: Write a program to mine a file and find out whether it contains 'python'.
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

with open("Code With Harry\9. File IO\donkey.txt", "r") as f:
    content = f.read()
    if "python" in content:
        print("Yes, the file contains 'python'.")
    else:
        print("No, the file does not contain 'python'.")

'''
Terminal - Ctrl + Shift + `
> python "path to the file"
'''
