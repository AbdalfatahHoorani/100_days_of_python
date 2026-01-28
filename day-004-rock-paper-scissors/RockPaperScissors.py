import random
import choices

number_chosen = int(input("what do you choose? type 0 (rock), 1 (paper), 2 (scissors)"))

random_choice = int(random.randint(0,2))

if number_chosen == random_choice:
    print(choices.list_of_things[number_chosen] + "\n" + choices.list_of_things[random_choice])
    print("we got a draw!")
elif number_chosen == 0 and random_choice == 1:
    print(choices.list_of_things[number_chosen] + "\n" + choices.list_of_things[random_choice])
    print("You Lost!")
elif number_chosen == 0 and random_choice == 2:
    print(choices.list_of_things[number_chosen] + "\n" + choices.list_of_things[random_choice])
    print("You Won!")
elif number_chosen == 1 and random_choice == 2:
    print(choices.list_of_things[number_chosen] + "\n" + choices.list_of_things[random_choice])
    print("You Lost!")
elif number_chosen == 1 and random_choice == 0:
    print(choices.list_of_things[number_chosen] + "\n" + choices.list_of_things[random_choice])
    print("You Won!")
elif number_chosen == 2 and random_choice == 0:
    print(choices.list_of_things[number_chosen] + "\n" + choices.list_of_things[random_choice])
    print("You Lost!")
elif number_chosen == 2 and random_choice == 1:
    print(choices.list_of_things[number_chosen] + "\n" + choices.list_of_things[random_choice])
    print("You Won!")

print(number_chosen, random_choice)

