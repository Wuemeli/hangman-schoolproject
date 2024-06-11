import random
import requests

word_listraw = requests.get("https://random-word-api.herokuapp.com/word?number=1")
word_list = word_listraw.json()
word = random.choice(word_list)

loses = 0
already_guessed = []

def check_win(word, already_guessed):
    for letter in word:
        if letter not in already_guessed:
            return False
    return True

def print_hangman(loses):
    if loses == 6:
        print("""
        +---+
        |   |
            |
            |
            |
        ==========""")
    elif loses == 5:
        print("""
        +---+
        |   |
        O   |
            |
            |
        ==========""")
    elif loses == 4:
        print("""
        +---+
        |   |
        O   |
        |   |
            |
        ==========""")
    elif loses == 3:
        print("""
        +---+
        |   |
        O   |
       /|   |
            |
        ==========""")
    elif loses == 2:
        print("""
        +---+
        |   |
        O   |
       /|\  |
            |
        ==========""")
    elif loses == 1:        
        print("""
        +---+
        |   |
        O   |
       /|\  |
       /    |
        ==========""")
    elif loses == 0:
        print("""
        +---+
        |   |
        O   |
       /|\  |
       / \  |
        ==========""")

print("""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
""")

print(word)
print_hangman(loses)
print("_" * len(word))

while loses < 6:
    userInput = input("Enter a letter: ").lower()
    
    if userInput in word:
        if userInput in already_guessed:
            print("Already guessed letters: ", already_guessed)
            print("You have already guessed that letter.")

            print_hangman(loses)
        else:
            print("You guessed correctly!")
            for i in range(word.count(userInput)):
                already_guessed.append(userInput)
        
        print("Already guessed letters: ", already_guessed)
        print_hangman(loses)
        
        if check_win(word, already_guessed):
            print("Congratulations You have won!")
            break
            
    else:
        loses += 1
        print("You guessed wrong. You have", 6 - loses, "tries left.")
        print("Already guessed letters: ", already_guessed)
        print_hangman(loses)
        
if loses == 6:
    print("You have lost. The word was", word)

