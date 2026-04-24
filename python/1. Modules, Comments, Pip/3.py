'''
> Date Created: 24/04/2026
> Author: Ishaan Rastogi
> Purpose: To speak the text entered by the user using pyttsx3
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

# pip install pyttsx3

import pyttsx3

engine = pyttsx3.init()
text = input("Enter what you want me to say: ")
engine.say(text)
engine.runAndWait()