'''
> Date Created: 20/07/2025
> Author: Ishaan Rastogi
> Purpose: To print a table in reverse order using for loop
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

n = int(input("Enter the number: "))

# i = 0, i = 1, ..., i = 10 => 10, 9, 8, ..., 0
for i in range(11): # range(11) generates numbers from 0 to 10
    print(f"{n} x {10 - i} = {n * (10 - i)}")