'''
> Date Created: 02/07/2025
> Author: Ishaan Rastogi
> Purpose: To print the contents of a directory using os module.
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working

NOTES- os is a built-in module in Python, no need to install it.
'''

import os

# Get the current working directory
current_directory = os.getcwd()
print(f"Current Directory: {current_directory}")

# List all files and directories in the current directory
files_and_directories = os.listdir(current_directory)
print("Files and Directories:")
for item in files_and_directories:
    print(item)

# Change to a specific directory let's say Code With Harry/1. Modules, Comments, Pip
target_directory = "Code With Harry/1. Modules, Comments, Pip"
os.chdir(target_directory)
print(f"Changed Directory to: {os.getcwd()}")

# List all files and directories in the target directory
files_and_directories = os.listdir(".")
print("Files and Directories in Target Directory:")
for item in files_and_directories:
    print(item)