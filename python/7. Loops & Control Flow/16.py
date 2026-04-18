'''
> Date Created: 20/07/2025
> Author: Ishaan Rastogi
> Purpose: To print star pattern
*****
 ***
  *  for n = 3
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

'''

i = 0 , 5 star, 0 space
i = 1 , 3 star, 1 space
i = 2 , 1 star, 2 spaces for n = 3

'''

n = int(input("Enter the number of rows: "))
for i in range(n+1):
    print(" " * (i), end="") # to print spaces
    print("*" * (2*(n-i)-1)) # to print stars