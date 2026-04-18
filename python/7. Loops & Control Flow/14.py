'''
> Date Created: 20/07/2025
> Author: Ishaan Rastogi
> Purpose: To print star pattern
  *
 * *
* * * for n = 3
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

'''
For n = 3, => Taking n+1 rows
1st row, 1 star, 2 outside spaces
2nd row, 2 stars, 1 outside spaces
3rd row, 3 stars, 0 outside space for n = 3

'''

n = int(input("Enter the number of rows: "))
for i in range(n+1):
    print(" " * (n-i), end="") # to print spaces
    print("* " * (i)) # to print stars with an inside space after each star