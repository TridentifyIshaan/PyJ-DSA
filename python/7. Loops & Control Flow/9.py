'''
> Date Created: 20/07/2025
> Author: Ishaan Rastogi
> Purpose: To print star pattern
  *
 ***
***** for n = 3
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

'''

1st place, 1 star, 2 spaces
2nd place, 3 star, 1 space
3rd place, 5 star, 0 spaces for n = 3

'''

n = int(input("Enter the number of rows: "))
for i in range(n+1):
    print(" " * (n-i), end="") # to print spaces
    print("*" * (2*i-1)) # to print stars