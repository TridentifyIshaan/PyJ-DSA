'''
> Date Created: 18/07/2025
> Author: Ishaan Rastogi
> Purpose: To write a python program to find the largest of 4 numbers entered by the user.
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

a1 = int(input("Enter a number 1: "))
a2 = int(input("Enter a number 2: "))
a3 = int(input("Enter a number 3: "))
a4 = int(input("Enter a number 4: "))

if ( a1 > a2 and a1 > a3 and a1 > a4 ):
    print(f"{a1} is the largest number") # f-string for formatting - or basic code is print(a1, "is the largest number")
elif ( a2 > a1 and a2 > a3 and a2 > a4 ):
    print(f"{a2} is the largest number")
elif ( a3 > a1 and a3 > a2 and a3 > a4 ):
    print(f"{a3} is the largest number")
elif ( a4 > a1 and a4 > a2 and a4 > a3 ):
    print(f"{a4} is the largest number")
else:
    print("All numbers are equal or invalid input")
print()