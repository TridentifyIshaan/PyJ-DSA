'''
> Date Created: 20/07/2025
> Author: Ishaan Rastogi
> Purpose: To print names starting with a given letter from a list
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

s = input("Enter a letter to print names starting with it: ")
l = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Ian", "Jack"]
print(f"Names starting with '{s}':")
for i in l:
    if i.lower().startswith(s):
        print(i)
print("Names printed successfully!")

# similar to startswith(), we have endswith() function.