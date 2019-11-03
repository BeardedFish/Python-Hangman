# Library imports
import os
import random

# The amount of attempts the user has failed trying to guess a letter or the secret word
attempts = 0

# The total amount of attempts possible before game over
total_attempts = 6

# Method for clearing the console screen
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# Method for printing the man being hanged onto the console output depending on the amount of attempts the user has failed guessing
def print_man():
    if attempts == 0:
        print()
        print(" -----------------")
        print(" |               |")
        print(" |                ")
        print(" |                ")
        print(" |                ")
        print(" |                ")
        print(" |                ")
        print("---               ")
        print()
    elif attempts == 1:
        print()
        print(" -----------------")
        print(" |               |")
        print(" |               O")
        print(" |                ")
        print(" |                ")
        print(" |                ")
        print(" |                ")
        print("---               ")
        print()
    elif attempts == 2:
        print()
        print(" -----------------")
        print(" |               |")
        print(" |               O")
        print(" |               |")
        print(" |                ")
        print(" |                ")
        print(" |                ")
        print("---               ")
        print()
    elif attempts == 3:
        print()
        print(" -----------------")
        print(" |               |")
        print(" |               O")
        print(" |              /|")
        print(" |                ")
        print(" |                ")
        print(" |                ")
        print("---               ")
        print()
    elif attempts == 4:
        print()
        print(" -----------------")
        print(" |               |")
        print(" |               O")
        print(" |              /|\\")
        print(" |                ")
        print(" |                ")
        print(" |                ")
        print("---               ")
        print()
    elif attempts == 5:
        print()
        print(" -----------------")
        print(" |               |")
        print(" |               O")
        print(" |              /|\\")
        print(" |              / ")
        print(" |                ")
        print(" |                ")
        print("---               ")
        print()
    else: # Basically means game over
        print()
        print(" -----------------")
        print(" |               |")
        print(" |               O")
        print(" |              /|\\")
        print(" |              / \\")
        print(" |                ")
        print(" |                ")
        print("---               ")
        print()

# The word bank for the hangman game
word_bank = [ "darian", "benam", "github", "programming", "python", "hangman", "pickles", "cake", "penguin", "bird", "computer" ]

# Get a random word from the word bank and store it
secret_word = random.choice(word_bank)
output_word = []

for char in secret_word:
    output_word.append("_")

# String variable for reporting feedback to the user based on their input
feedback = ""

# List to keep track of letters that have already been guessed
guessed_chars = []

# Main game loop
while True:
    # Clear the console screen
    cls()

    # Print program title
    print("Hangman - Python Version | By: Darian Benam\n")

    # Print the values in output_word
    print("Guess the word: ", end = "")
    for char in output_word:
        print(char + " ", end = "")
    print()

    # Print the already guessed letters in guessed_chars
    print("\nUsed letters: ", end = "")
    for char in guessed_chars:
        print(char + " ", end = "")
    print()

    # Print the state of the man
    print_man()

    # Check if attempts are greater than or equal to total_attempts. If it is, game over!
    if attempts >= total_attempts:
        print("Game over!")
        break

    # Check if the secret_word is equal to the output_word after modification
    if secret_word == "".join(output_word):
        print("Congratulations, you guessed the correct word!")
        break

    # Print out any feedback the game has to tell the player if it has a value in it
    if feedback:
        print(feedback + "\n")
        feedback = ""

    # Get the guess from the user
    guess = input("Enter your guess: ").lower()

    if len(guess) == 0: # No guess was entered
        feedback = "Please enter a guess!"
    elif len(guess) == 1: # Guess is a letter
        # Prevent the user from re-using a letter that they previously guessed
        if guess in guessed_chars:
            feedback = "You already guessed that character! Please try again."
            continue

        # Add the letter to the list of guessed characters
        guessed_chars.append(guess)

        if not guess in secret_word:
            attempts += 1
            feedback = "The word does not contain the letter '" + guess + "'. Try a different letter."
            continue
        else:
            feedback = "The word did contain the letter '" + guess + "'. Nice work, keep it up!"

        # Check if the the guessed letter is in the secret_word, if it is, replace the output_word index with that letter
        for i in range(0, len(secret_word), 1):
            if guess in secret_word[i]:
                output_word[i] = guess
    else: # Guess is a word
        if guess == secret_word:
            output_word = secret_word 
            print("Congratulations, you guessed the correct word!")
            break
        else:
            attempts += 1
            feedback = "The word is not '" + guess + "'. Try something else."

# Prevent the program from closing automatically
input("\nPress <ENTER> to close the program.")
