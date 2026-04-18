'''
> Date Created: 20/07/2025
> Author: Ishaan Rastogi
> Purpose: To print a given number in repition using loops
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

# We will take input as a string so that the number gets concatenated and the pattern gets printed
n = input("Enter a number to print the pattern for: ")
i = int(input("Enter how many times you want to print the number: "))
for i in range(i + 1): # This loop is for the number of lines
    for j in range(i): # This loop is for number and spaces
        print(n, end=" ")
    print() # Number of new lines
print("Pattern printed successfully!")