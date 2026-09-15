'''
> Date Created: 01/08/2026
> Dates of Update: 13/09/2026
> Author: Ishaan Rastogi
> Purpose: To count the digits of a non-negative number.
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

def count_digits(num, count=0):
    while (num > 0):
        count += 1
        last_digit = num%10 # extracting last digit by doing calculating remainder
        num = num//10 # removing last digit by doing floor division
    return count
print(count_digits(12345))