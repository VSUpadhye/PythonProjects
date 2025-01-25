import random

def deal_cards():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calc_score(values):
    """Gives the total score"""
    total = sum(values)
    if total == 21 and len(values) == 2:
        return 0
    if total > 21 and 11 in values:
        values.remove(11)
        values.append(1)
    total = sum(values)
    return total

def blackjack_game():
    blackjack_dictionary = {"user" : [], "comp" : []}
    for i in range(2):
        blackjack_dictionary['user'].append(deal_cards())
        blackjack_dictionary['comp'].append(deal_cards())

    user_total = 0
    comp_total = 0
    get_card = 'y'
    while get_card == 'y':
        user_total = calc_score(blackjack_dictionary['user'])
        print(f"Your cards: {blackjack_dictionary['user']}, current score: {user_total}")

        comp_total = calc_score(blackjack_dictionary['comp'])
        print(f"Computer's first card: {blackjack_dictionary['comp'][0]}")
        get_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if get_card == 'y':
            blackjack_dictionary['user'].append(deal_cards())
    while comp_total < 17 and comp_total != 0:
        blackjack_dictionary['comp'].append(deal_cards())
        comp_total = calc_score(blackjack_dictionary['comp'])
    print(f"Your final hand: {blackjack_dictionary['user']}, final score: {user_total}")
    print(f"Computer's final hand: {blackjack_dictionary['comp']}, final score: {comp_total}")
    
    if user_total == 0 and comp_total == 21:
        print("You win!")
    elif comp_total == 0 and user_total == 21:
        print("You lose!")
    elif user_total > 21:
        print("You lose.")
    elif comp_total > 21:
        print("You win!")
    elif user_total > comp_total:
        print("You win!")
    elif user_total == comp_total:
        print("Its a draw!")
    else:
        print("You lose.")

    again = input("Type 'yes' to go again, otherwise type 'no': ")
    if again == 'yes':
        print("\n" * 20)
        blackjack_game()

start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if start == 'y':
    blackjack_game()