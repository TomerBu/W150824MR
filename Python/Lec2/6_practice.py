from random import choice
from hangman import HANGMANPICS

lives = len(HANGMANPICS) - 1
word_list = ["dog", "cat", "elephant", "home"]

chosen_word = choice(word_list)

#testing code
print(f'Pssst, the solution is {chosen_word}.')

display = ["_" for _ in chosen_word]

while "_" in display and lives > 0:
    print(display)
    print(HANGMANPICS[lives])
    guess = input("Guess a letter: ").lower()

    if guess not in chosen_word:
        lives -= 1
    else:
        # update the display
        for i in range(len(chosen_word)):
            if guess == chosen_word[i]:
                display[i] = guess

if lives > 0:
    print("You win!")
else:
    print("You lose!")