'''
> Date Created: 15/09/2026
> Dates of Update: 
> Author: Ishaan Rastogi
> Purpose: To reverse a list/array using while loop
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

num = [5,7,3,2,6,1,5,9]
l = 0
r = len(num) - 1

def reverseArr(num, l, r): # array, left pointer, right pointer
    while l < r:
        num[l], num[r] = num[r], num[l] # swap the elements
        # Moving pointers
        l += 1
        r -= 1
    return num
print(reverseArr(num, 2, 5))