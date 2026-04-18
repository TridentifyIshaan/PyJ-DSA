'''
> Date Created: 31/07/2025
> Author: Ishaan Rastogi
> Purpose: To read the text from a given file 'poems.txt' and find out whether it contains the word 'twinkle'.
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

with open(r'Code With Harry\9. File IO\poems.txt', 'r') as f:
    content = f.read()
    if 'twinkle' in content:
        print("Yes, the word 'twinkle' is present in the file.")
    else:
        print("No, the word 'twinkle' is not present in the file.")

'''
Terminal - Ctrl + Shift + `
> python "path to the file"
'''
