'''
> Date Created: 20/07/2025
> Author: Ishaan Rastogi
> Purpose: To print the sum of the first n natural numbers using loops
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

n = int(input("Enter a number to print the sum of first n natural numbers: "))
sum = 0
for i in range(n+1):
    sum += i
print(f"The sum of the first {n} natural numbers is: {sum}") 