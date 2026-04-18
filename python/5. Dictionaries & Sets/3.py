'''
> Date Created: 17/07/2025
> Author: Ishaan Rastogi
> Purpose: To create a dictionary of Hindi words with values as their English translation and provide user with an option to search for a word
> Operating System: This is only for Windows OS, it may or may not work on other OS
> Program Status: 100% Working
'''

# Hindi to English Dictionary
dictionary = {
    "Hello": "नमस्ते",
    "Thank you": "धन्यवाद",
    "Please": "कृपया",
    "Best wishes": "शुभकामनाएँ",
    "Good morning": "सुप्रभात",
    "Good night": "शुभ रात्रि",
    "How are you?": "आप कैसे हैं?",
    "Excuse me": "मुझे माफ करें",
    "Absolutely": "बिल्कुल",
    "Okay": "ठीक है"
}

word = input("Enter an English word to translate: ")
print(dictionary[word]) # Output: Hindi translation of the word