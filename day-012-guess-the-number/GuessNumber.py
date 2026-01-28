import random


def PlayGame():
    computer_choice = random.randint(1,100)

    if input("please choose difficult, 'easy' or 'hard'").lower() == 'easy':
        lives = 10
        print("you got 10 lives")
    elif input("please choose difficult, 'easy' or 'hard'").lower() == 'hard':
        lives = 5
        print("you got 5 lives")
    else:
        lives = 0
        print("did you make a mistake?")

    
    while lives != 0:
        user_guess = int(input(f"Guess a number. You got {lives} attempts."))

        if user_guess < 1 or user_guess > 100:
            print("choose numbers between 1-100. NOT HIGHER NOT LOWER!!")
        elif(user_guess < computer_choice):
            print("Your guess is too low.")
            lives -= 1
        elif(user_guess > computer_choice):
            print("Your guess is too high.")
            lives -= 1
        elif(user_guess == computer_choice):
            print("You've guessed correctly!!")
        elif lives - 1 == 0:
            lives -= 1
            print("You have lost at this game")
            if input("would you like to play again? 'y' or 'n'").lower == 'n':
                return "to was nice having you!"
            else:
                if input("please choose difficult, 'easy' or 'hard'").lower() == 'easy':
                    lives = 10
                    print("you got 10 lives")
                elif input("please choose difficult, 'easy' or 'hard'").lower() == 'hard':
                    lives = 5
                    print("you got 5 lives")
                else:
                    lives = 0
                    print("did you make a mistake?")
                print("here we go again!!")





PlayGame()
