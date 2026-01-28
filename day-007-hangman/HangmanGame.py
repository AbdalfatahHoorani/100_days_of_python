import random

stages = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

word_list = ["aardvark", "baboon", "camel"]
# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
chosen_word = word_list[random.randint(0,len(word_list)-1)]
print(chosen_word)
# guessed letters to for redundancy checking

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.
lives = 6
correct_guesses = []
for n in range(0, len(chosen_word)):
    correct_guesses.append('_')

print(" ".join(correct_guesses))

nice_choice = False
already_chosen = []
print(stages[0])
stage_level = 0
while lives != 0:
    guess = input("please choose one letter!").lower()

    if guess in already_chosen:
        print("you've already choose this letter try something else")
        continue
    else:
        already_chosen.append(guess)


    for n in range(0, len(chosen_word)):
        if guess == chosen_word[n]:
            correct_guesses[n] = guess
            nice_choice = True
    if nice_choice:
        print("you made the correct guess")
    else:
        lives -=1
        stage_level += 1
        print(f"your guess was wrong :( lives remaining {lives}")

    nice_choice = False
    print(" ".join(correct_guesses))
    print(already_chosen)
    print(stages[stage_level])

    if "_" not in correct_guesses:
        print("You have won!")
        break
    elif lives == 0:
        print("you have lost!!")
        break



