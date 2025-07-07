import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
final_password = []

print("Welcome to the PyPassword Generator!")
check_number = True
total_characters = 0
choose_random = random.randint(1, 3)


while check_number:
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))
    total_characters = nr_numbers + nr_symbols + nr_letters
    if total_characters <= 0:
        print("please try giving something that is higher than 0!!!")
        total_characters = 0
    else:
        check_number = False

for number in range(0, total_characters):
    if choose_random == 1:
        random_letters = random.randint(0, 51)
        final_password.append(letters[random_letters])

    elif choose_random == 2:
        random_numbers = random.randint(0, 9)
        final_password.append(numbers[random_numbers])

    elif choose_random == 3:
        random_symbols = random.randint(0, 8)
        final_password.append(symbols[random_symbols])

    choose_random = random.randint(1, 3)

print("".join(final_password))

# WE CAN USE random.shuffle(my_list) rather than making 3 extra random integers
random.shuffle(final_password)
print("".join(final_password))


