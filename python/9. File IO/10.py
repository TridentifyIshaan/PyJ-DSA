'''
> Date Created: 31/07/2025
> Author: Ishaan Rastogi
> Purpose: A file contains a word 'Donkey' multiple times. You need to write a program which replace this word with ##### by updating the same file.
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

# r+ mode is used to read and write to the file. If the file does not exist, it will raise an error.

with open("Code With Harry\9. File IO\donkey.txt", "r+") as f:
    content = f.read()
    content = content.replace("Donkey", "######")
    f.seek(0) # Move the cursor to the beginning of the file
    f.write(content) # Write the updated content back to the file
    f.truncate() # Truncate the file to the current position, removing any remaining content after the write

'''
Terminal - Ctrl + Shift + `
> python "path to the file"
'''