'''
> Date Created: 02/07/2025
> Author: Ishaan Rastogi
> Purpose: To print a random joke using the pyjokes library
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

# pip install pyjokes
import pyjokes

print("Printing joke...")
joke = pyjokes.get_joke()
print(joke)