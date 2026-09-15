'''
> Date Created: 01/08/2026
> Dates of Update: 13/09/2026
> Author: Ishaan Rastogi
> Purpose: To count the digits of a non-negative number using log.
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

from math import log10

def count_digits(num):
    return int(log10(num)+1) # converting into integer format to strip out decimal values
print(count_digits(12345))