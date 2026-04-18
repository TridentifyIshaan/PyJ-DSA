'''
> Date Created: 20/07/2025
> Author: Ishaan Rastogi
> Purpose: To print the table of a given number using loops
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

n = int(input("Enter a number to print its table: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
print("Table printed successfully!")