import random

def word_guessing_game():
    words = ["python", "programming", "code", "computer", "algorithm"]
    word_to_guess = random.choice(words)
    guessed_word = "_" * len(word_to_guess)
    guesses = set()
    attempts = 6
    
    while "_" in guessed_word and attempts > 0:
        print("\nGuessed Word:", " ".join(guessed_word))
        guess = input("Enter a letter: ").lower()
        if guess in guesses:
            print("You've already guessed that letter!")
            continue
        guesses.add(guess)
        if guess not in word_to_guess:
            attempts -= 1
            print("Incorrect guess. Attempts left:", attempts)
        else:
            for i in range(len(word_to_guess)):
                if word_to_guess[i] == guess:
                    guessed_word = guessed_word[:i] + guess + guessed_word[i+1:]
    if "_" not in guessed_word:
        print("\nCongratulations! You guessed the word:", word_to_guess)
    else:
        print("\nOut of attempts. The word was:", word_to_guess)

if __name__ == "__main__":
    print("Welcome to the Word Guessing Game!")
    word_guessing_game()
