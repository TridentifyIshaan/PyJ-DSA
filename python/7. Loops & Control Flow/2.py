'''
> Date Created: 19/07/2025
> Author: Ishaan Rastogi
> Purpose: To show different types of control flow statements in Python.
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

# Control Flow Statements in Python

# Break Statement - to exit a loop abruptly
for i in range(11):
    if ( i == 5 ):
        break
    print(i)
print()

# Output: 0 1 2 3 4

# Continue Statement - to skip the current iteration and continue with the next
for i in range(11):
    if ( i == 5 ):
        continue
    print(i)
print()

# Output: 0 1 2 3 4 6 7 8 9 10 - Print all numbers except 5

# Pass Statement - a null operation, used when a statement is required syntactically but no action is needed

for i in range(11):
    pass  # This will do nothing - To skip the loop without any action
print()

i = 0
while( i < 5):
    print(i)
    i += 1