'''
> Date Created: 01/08/2026
> Dates of Update: 13/09/2026
> Author: Ishaan Rastogi
> Purpose: To reverse a number
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

def reverse_digits(num, result=0):
    while (num>0):
        id = num%10 # last digit
        result = result * 10 + id # appending last digit first
        num = num//10 # removing last digit
    return result
print(reverse_digits(12345))