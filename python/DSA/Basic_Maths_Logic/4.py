'''
> Date Created: 01/08/2026
> Author: Ishaan Rastogi
> Purpose: To check if a number is palindrome or not.
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

def isPalindrome(num, result=0):
    n = num
    while (num>0):
        id = num%10
        result = result * 10 + id
        num = num//10
    return result==n
print(isPalindrome(12321))