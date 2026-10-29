"""Console Hangman game for the CodeAlpha Python task."""
import random

WORDS = ["python", "coding", "laptop", "planet", "garden"]
MAX_WRONG_GUESSES = 6


def play_hangman():
    word = random.choice(WORDS)
    guessed_letters = set()
    wrong_guesses = 0

    print("\n=== Hangman Game ===")
    print(f"Guess the word. You can make {MAX_WRONG_GUESSES} incorrect guesses.")

    while wrong_guesses < MAX_WRONG_GUESSES:
        display = " ".join(letter if letter in guessed_letters else "_" for letter in word)
        print("\nWord:", display)
        print("Incorrect guesses left:", MAX_WRONG_GUESSES - wrong_guesses)

        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You guessed the word: {word}")
            return

        guess = input("Enter one letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one alphabetic letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)
        if guess in word:
            print("Correct!")
        else:
            wrong_guesses += 1
            print("That letter is not in the word.")

    print(f"Game over! The word was: {word}")


if __name__ == "__main__":
    play_hangman()
