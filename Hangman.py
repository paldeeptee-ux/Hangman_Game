import random

# List of predefined words
words = ["python", "computer", "apple", "school", "garden"]

# Select a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum incorrect guesses
incorrect_guesses = 0
max_guesses = 6

print("====== WELCOME TO HANGMAN ======")

while incorrect_guesses < max_guesses:

    display_word = ""

    # Display guessed letters and underscores
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if player has guessed the word
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    print("Incorrect guesses left:", max_guesses - incorrect_guesses)

    guess = input("Guess a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check guess
    if guess in word:
        print("✅ Correct!")
    else:
        incorrect_guesses += 1
        print("❌ Wrong!")

# If player loses
if incorrect_guesses == max_guesses:
    print("\n💀 Game Over!")
    print("The correct word was:", word)