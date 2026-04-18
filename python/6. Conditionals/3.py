'''
> Date Created: 18/07/2025
> Author: Ishaan Rastogi
> Purpose: To write a python program to satisfy the requirements of the task.
A student is required to secure minimum 30% marks to pass in End Semester Examination and
minimum aggregate marks of 35% to pass the course.
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

# This will show the concept of nested if statements
print("Welcome to the End Semester Examination Result Checker\nEnter your marks out of 60 for End Sem.\n")
marks = int(input("Enter marks: "))

if ( ((marks/60)*100) >= 30 ):
    print("\nNow, enter the total marks for the subject out of 100.")
    total_marks1 = int(input("Enter total marks: "))
    if ( total_marks1 >= 35 ):
        print("\nCongratulations! You have passed the course.")
    else:
        print("\nSorry! You have failed the course due to aggregate marks.")
else:
    print("\nSorry! You have failed the course due to End Semester Examination marks.")