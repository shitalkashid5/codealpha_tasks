import random

words = ["python", "computer", "programming", "developer", "software"]

word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("================================")
print("       HANGMAN GAME")
print("================================")

while wrong_guesses < max_wrong_guesses:

    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Wrong guesses:", wrong_guesses)
    print("Remaining chances:", max_wrong_guesses - wrong_guesses)

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess! ✅")
    else:
        wrong_guesses += 1
        print("Wrong guess! ❌")

    if all(letter in guessed_letters for letter in word):
        print("\n🎉 Congratulations! You Won!")
        print("The word was:", word)
        break

else:
    print("\n❌ Game Over!")
    print("The word was:", word)