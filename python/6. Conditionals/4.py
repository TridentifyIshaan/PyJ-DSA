'''
> Date Created: 18/07/2025
> Author: Ishaan Rastogi
> Purpose: To write a python program to satisfy the requirements of the task.
A spam comment is defined as a text containing following words:
"Make a lot of money", "buy now", "click this", "subscribe this"
Write a program to check if a comment is spam or not.
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

# This will show the concept of in & any keyword

print("Welcome to the Spam Comment Checker\nEnter your comment below:\n")
comment = input("Enter comment: ")
spam_keywords = ["make a lot of money", "buy now", "click this", "subscribe this"]

# Check if any spam keyword is present in the comment (case-insensitive)
# Significance of any keyword is that it will check if any of the keywords are present in the comment, it will flag it as spam if you haven't used it, then it will only flag the comments looking exactly like spam_keywords.

if any(keyword in comment.lower() for keyword in spam_keywords):
    print("This comment is a spam comment.")
else:
    print("This comment is not a spam comment.")