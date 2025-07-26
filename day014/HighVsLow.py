import random
from game_data import data

#make them global because we will use them in functions
RANDOM_PICK_ONE = random.randint(0, 49)
RANDOM_PICK_TWO = random.randint(0, 49)
asked_about = [RANDOM_PICK_ONE, RANDOM_PICK_TWO]


#to keep checking that the two values are random
def NotEqual():
    global RANDOM_PICK_TWO
    while RANDOM_PICK_ONE == RANDOM_PICK_TWO:
        RANDOM_PICK_TWO = random.randint(0,49)

#a function to make sure that we don't make redundant questions
def AlreadyAskedAbout():
    global RANDOM_PICK_TWO
    global asked_about
    while RANDOM_PICK_TWO in asked_about or RANDOM_PICK_TWO == RANDOM_PICK_ONE:
        RANDOM_PICK_TWO = random.randint(0,49)
    asked_about.append(RANDOM_PICK_TWO)




def PlayGame():
    global RANDOM_PICK_TWO
    global RANDOM_PICK_ONE
    # two random picks from the game data
    #make sure that the two picks are different from each other
    NotEqual()
    pick_one = data[RANDOM_PICK_ONE]
    pick_two = data[RANDOM_PICK_TWO]


    #this while loop is to compare and check the follower count while alive!
    score = 0
    alive = True
    while alive:
        print(pick_one['name'] + " " + pick_one['description'])
        print(pick_two['name'] + " " + pick_two['description'])
        user_guess = input("which do you think has more followers on Instagram? please type '1' or '2'")
        if user_guess == '1':
            if pick_one['follower_count'] > pick_two['follower_count']:
                print("\n" * 10)
                print("correct")
                score += 1
                #now we need to save whatever we got in an array for us to not as about it again
                #then we need to remove the choice with the lower follower count and keep what we chose
                #and compare it with something else
                RANDOM_PICK_TWO = random.randint(0, 49)
                NotEqual()
                AlreadyAskedAbout()
                pick_two = data[RANDOM_PICK_TWO]

            else:
                print(f"Wrong, you got {score} questions correct")
                again = input("would you like to play again? y or n")
                if  again == 'y':
                    print("\n" * 10)
                    score = 0
                    RANDOM_PICK_TWO = random.randint(0, 49)
                    RANDOM_PICK_ONE = random.randint(0, 49)
                    NotEqual()
                    AlreadyAskedAbout()
                    pick_one = data[RANDOM_PICK_ONE]
                    pick_two = data[RANDOM_PICK_TWO]
                else:
                    alive = False
        elif user_guess == '2':
            if pick_two['follower_count'] > pick_one['follower_count']:
                print("\n" * 10)
                print("correct")
                score += 1
                #do the same as pick '1' but now we need to move pick 2 to pick 1 then re-roll pick 2
                pick_one = pick_two
                RANDOM_PICK_TWO = random.randint(0, 49)
                NotEqual()
                AlreadyAskedAbout()
                pick_two = data[RANDOM_PICK_TWO]

            else:
                print("\n" * 10)
                print(f"Wrong, you got {score} questions correct")
                again = input("would you like to play again? y or n")
                if  again == 'y':
                    print("\n" * 10)
                    score = 0
                    RANDOM_PICK_TWO = random.randint(0, 49)
                    RANDOM_PICK_ONE = random.randint(0, 49)
                    NotEqual()
                    AlreadyAskedAbout()
                    pick_one = data[RANDOM_PICK_ONE]
                    pick_two = data[RANDOM_PICK_TWO]
                else:
                    alive = False






PlayGame()
