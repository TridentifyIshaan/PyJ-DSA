'''
> Date Created: 03/08/2025
> Author: Ishaan Rastogi
> Purpose: Write a program to find out the line number where python is present from ques 6.
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

lineno = 1 # we will start counting lines from 1

with open("Code With Harry\9. File IO\donkey.txt", "r") as f:
    content = f.readlines() # Replace read with readlines
    for line in content:
        if "python" in line:
            print(f"'python' is found at line number: {lineno}")
            break;
        lineno += 1 # Increment the line number after each iteration
    else:
        print("No, the file does not contain 'python'.")
        
'''
Terminal - Ctrl + Shift + `
> python "path to the file"
'''
