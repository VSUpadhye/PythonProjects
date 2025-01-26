import random

def final_result(u_list, c_list, u_total, c_total):
    print(f"Your final hand: {u_list}, final score: {u_total}")
    print(f"Computer's final hand: {c_list}, final score: {c_total}")

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

def compare(user_score, comp_score):
    if user_score == 0 and comp_score == 21:
        print("You win with a blackjack!")
    elif comp_score == 0 and user_score == 21:
        print("You lose, dealer has a blackjack!")
    elif user_score > 21 or comp_score == 0:
        print("You lose.")
    elif comp_score > 21 or user_score == 0:
        print("You win!")
    elif user_score > comp_score:
        print("You win!")
    elif user_score == comp_score:
        print("Its a draw!")
    else:
        print("You lose.")


def blackjack_game():
    blackjack_dictionary = {"user" : [], "comp" : []}
    for i in range(2):
        blackjack_dictionary['user'].append(deal_cards())
        blackjack_dictionary['comp'].append(deal_cards())

    user_total = -1
    comp_total = -1
    get_card = 'y'
    while get_card == 'y':
        user_total = calc_score(blackjack_dictionary['user'])
        print(f"Your cards: {blackjack_dictionary['user']}, current score: {user_total}")

        comp_total = calc_score(blackjack_dictionary['comp'])
        print(f"Computer's first card: {blackjack_dictionary['comp'][0]}")
        if user_total > 21:
            final_result(blackjack_dictionary['user'], blackjack_dictionary['comp'], user_total, comp_total)
            print("You went over. You lose.")
            exit()
        get_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if get_card == 'y':
            blackjack_dictionary['user'].append(deal_cards())

    while comp_total < 17 and comp_total != 0:
        blackjack_dictionary['comp'].append(deal_cards())
        comp_total = calc_score(blackjack_dictionary['comp'])
    final_result(blackjack_dictionary['user'], blackjack_dictionary['comp'], user_total, comp_total)
    compare(user_total, comp_total)

    again = input("Type 'yes' to go again, otherwise type 'no': ")
    if again == 'yes':
        print("\n" * 20)
        blackjack_game()

start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if start == 'y':
    blackjack_game()