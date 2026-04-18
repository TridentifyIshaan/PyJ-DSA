'''
> Date Created: 02/07/2025
> Author: Ishaan Rastogi
> Purpose: To convert text to speech using gTTS (Google Text-to-Speech)
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working

NOTES- pip install gtts

    Additionaly install an extension called audio-preview by sukumo28
    https://marketplace.visualstudio.com/items?itemName=sukumo28.wav-preview
'''

from gtts import gTTS

text = "I am a programmer, I write code"
tts = gTTS(text)
tts.save("Code With Harry/1. Modules, Comments, Pip/output.mp3")
print("Speech saved to output.mp3")