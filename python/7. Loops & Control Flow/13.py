'''
> Date Created: 20/07/2025
> Author: Ishaan Rastogi
> Purpose: To print star pattern
***
 **
  * for n = 3
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

'''
For n = 3, => Taking n+1 rows
i = 0, print 3 stars, 0 space
i = 1, print 2 stars, 1 spaces
i = 2, print 1 star, 2 spaces for n = 3
'''

n = int(input("Enter the number of rows: "))
for i in range(n+1):
  print(" " * i, end="") # to print spaces
  print("*" * (n-i)) # to print stars