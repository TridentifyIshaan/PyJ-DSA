'''
> Date Created: 03/08/2025
> Author: Ishaan Rastogi
> Purpose: Repeat program 4 for a list of such words to be censored.
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

# List of words to censor
censor_words = ["Donkey", "Elephant", "Giraffe"]

with open("Code With Harry\9. File IO\donkey.txt", "r+") as f:
    content = f.read()
    for word in censor_words:
        content = content.replace(word, "#"*len(word))
    f.seek(0) # Move the cursor to the beginning of the file
    f.write(content) # Write the updated content back to the file
    f.truncate() # Truncate the file to the current position, removing any remaining content after the write

'''
Terminal - Ctrl + Shift + `
> python "path to the file"
'''