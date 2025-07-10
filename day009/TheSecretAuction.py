# TODO-1: Ask the user for input
dictionary_of_players = {"abood": 10}
while True:
    player_name = input("Please give us your name.")
    player_bid = input("Please tell us how much you would like to bid.")
    # TODO-2: Save data into dictionary {name: price}
    dictionary_of_players [player_name] = player_bid
    print("\n" * 20)

    go_again = input("Would you like to add another player? 'yes' or 'no'")
    if go_again.lower() == 'no':
        break

highest_bidder = ""
highest_bid = 0
for key in dictionary_of_players:
    if  int(dictionary_of_players[key]) > highest_bid:
        highest_bid = int(dictionary_of_players[key])
        highest_bidder = key


print(f"{highest_bidder} is the highest bidder: {highest_bid}")
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


