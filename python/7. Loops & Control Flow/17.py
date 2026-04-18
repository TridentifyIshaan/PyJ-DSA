'''
> Date Created: 20/07/2025
> Author: Ishaan Rastogi
> Purpose: To print star pattern
* * *
*   *
* * *  for n = 3
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

n = int(input("Enter the number of rows: "))
for i in range(n):
  if i == 0 or i == n - 1:
    print("* " * n)
  else:
    print("* " + "  " * (n - 2) + "*")
