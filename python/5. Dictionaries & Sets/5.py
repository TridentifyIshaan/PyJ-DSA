'''
> Date Created: 17/07/2025
> Author: Ishaan Rastogi
> Purpose: To find value of s:
            s = set()
            s.add(20)
            s.add(20.0)
            s.add("20")
            print(s)
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

s = set()
s.add(20)
s.add(20.0)
s.add("20")
print(s)

# Well, 20 == 20.0, so they are considered the same value in a set.