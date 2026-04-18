'''
> Date Created: 10/08/2025
> Author: Ishaan Rastogi
> Purpose: Write a program to find out whether a file is identical & matches the content of another file.
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

with open (r"I:\My Drive\CS 100\Py-Lang\Code With Harry\9. File IO\poems.txt", "r") as f1:
    content1 = f1.read()

with open (r"I:\My Drive\CS 100\Py-Lang\Code With Harry\9. File IO\poems_copy.txt", "r") as f2:
    content2 = f2.read()

if content1 == content2:
    print("The files are identical and match the content.")
else:
    print("The files are not identical or do not match the content.")

'''
Terminal - Ctrl + Shift + `
> python "path to the file"
'''
