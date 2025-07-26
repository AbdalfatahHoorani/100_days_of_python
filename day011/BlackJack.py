import random
import art

def AdjustForAce(total, visible_cards):
    ace_count = visible_cards.count("ace")
    while total > 21 and ace_count > 0:
        total -= 10
        ace_count -= 1
    return total

def WinOrBustOrDraw(player_cards, dealer_cards):
    if player_cards == 21:
        print("BLACK JACK!")
        return True
    elif player_cards > 21:
        print("Player Busted!")
        return True
    elif dealer_cards > 21:
        print("Dealer Busted! YOU WON!!")
        return True
    elif player_cards > dealer_cards:
        print("YOU WON!!")
        return True
    elif player_cards < dealer_cards:
        print("you lost :(")
        return True
    else:
        print("it's a draw!")
        return True

def WillDealerHit(dealer_value, player_value):
    return dealer_value < 17 or (dealer_value < player_value and dealer_value < 21)

def RandomCardGeneration_CardName(list_of_available_options):
    return random.choice(list(list_of_available_options.keys()))

def PlayGame():
    print(art.logo)

    cards = {
        "ace": 11,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "jack": 10,
        "queen": 10,
        "king": 10,
    }

    while True:
        player_hand = [RandomCardGeneration_CardName(cards), RandomCardGeneration_CardName(cards)]
        dealer_hand = [RandomCardGeneration_CardName(cards)]

        player_total = sum([cards[c] for c in player_hand])
        dealer_total = sum([cards[c] for c in dealer_hand])

        player_total = AdjustForAce(player_total, player_hand)
        dealer_total = AdjustForAce(dealer_total, dealer_hand)

        print(f"\nPlayer's cards: {', '.join(player_hand)} | Total: {player_total}")
        print(f"Dealer's visible card: {', '.join(dealer_hand)} | Total: {dealer_total}")

        # Player Turn
        while True:
            player_choice = input("Please pick what you want to do next, stand or hit? ").lower()
            if player_choice == "hit":
                card = RandomCardGeneration_CardName(cards)
                player_hand.append(card)
                player_total += cards[card]
                player_total = AdjustForAce(player_total, player_hand)
                print(f"You drew: {card}")
                print(f"Player's cards: {', '.join(player_hand)} | Total: {player_total}")
                if player_total > 21:
                    print("You busted!")
                    break
            elif player_choice == "stand":
                break
            else:
                print("Invalid input. Choose 'stand' or 'hit'.")

        # Dealer Turn
        while WillDealerHit(dealer_total, player_total):
            card = RandomCardGeneration_CardName(cards)
            dealer_hand.append(card)
            dealer_total += cards[card]
            dealer_total = AdjustForAce(dealer_total, dealer_hand)

        print(f"\nFinal Hands:")
        print(f"Player's cards: {', '.join(player_hand)} | Total: {player_total}")
        print(f"Dealer's cards: {', '.join(dealer_hand)} | Total: {dealer_total}")
        WinOrBustOrDraw(player_total, dealer_total)

        if input("\nWould you like to play again? 'yes' or 'no': ").lower() != 'yes':
            print("Thanks for playing!")
            break

# Run the game

PlayGame()
