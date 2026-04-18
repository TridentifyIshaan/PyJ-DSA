'''
> Date Created: 31/07/2025
> Author: Ishaan Rastogi
> Purpose: To generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder.
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

def generateTable(n):
    with open(f"Code With Harry\9. File IO\Tables\Table_of_{n}.txt", "w") as f:
        for i in range(1, 11):
            f.write(f"{n} x {i} = {n * i}\n")

for i in range (2, 21):
    generateTable(i)

'''
Terminal - Ctrl + Shift + `
> python "path to the file"
'''