'''
> Date Created: 01/08/2026
> Dates of Update: 13/09/2026
> Author: Ishaan Rastogi
> Purpose: To check if a number is palindrome or not.
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

# Number palindrome
def isPalindrome(num, result=0):
    n = num # saving so that we can keep the original value also along with the reversed number
    while (num>0):
        id = num%10 # last digit
        result = result * 10 + id # appending last digit first
        num = num//10 # removing last digit
    return result==n
print(isPalindrome(12321))