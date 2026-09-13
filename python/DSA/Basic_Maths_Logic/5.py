'''
> Date Created: 01/08/2026
> Dates of Update: 13/09/2026
> Author: Ishaan Rastogi
> Purpose: To check if a number is armstrong or not.
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

from math import log10

# counting length of a number
def count_digits(num):
    return int(log10(num)+1)

def isArmstrong(num, sum=0):
    n = num
    while (n>0):
        id = n%10 # last digit
        sum = sum + id ** count_digits(num) # sum of power of individual digit but in reverse
        n = n//10 # removing last digit
    return sum==num
print(isArmstrong(1634))