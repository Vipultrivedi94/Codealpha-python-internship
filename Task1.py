# Python internship 

# Codealpha task 1 Hangman game 
 
import random

words = ["python", "coding", "developer", "computer", "program"]

word = random.choice(words)

guessed_letters = []
attempts = 6

print("🎮 Welcome to Hangman Game!")
print("Guess the word letter by letter")
print("You have 6 wrong chances\n")

hidden_word = ["_"] * len(word)

while attempts > 0:

    print("Word:", " ".join(hidden_word))
    print("Wrong attempts left:", attempts)
    print("Guessed letters:", guessed_letters)

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter\n")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter\n")
        continue


    guessed_letters.append(guess)

    if guess in word:

        print("Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                hidden_word[i] = guess

    else:
        attempts -= 1
        print(" Wrong guess!")
    print()

    if "_" not in hidden_word:
        print("Congratulations! You won!")
        print("The word was:", word)
        break

if "_" in hidden_word:
    print(" Game Over!")
    print("The word was:", word)