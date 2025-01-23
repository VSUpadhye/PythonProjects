import art

print(art.logo)

blind_auction = {}

new_bidder = "yes"
while new_bidder == "yes":
    # TODO-1: Ask the user for input
    name = input("Enter bidder's name: ")
    # TODO-2: Save data into dictionary {name: price}
    blind_auction[name] = int(input("Enter the price: $"))
    # TODO-3: Whether if new bids need to be added
    new_bidder = input("Type 'yes' if there are any other bids. Otherwise type 'no'.\n")
    print("\n" * 10)
# TODO-4: Compare bids in dictionary
highest_bid = 0
#winner = ""
# for key in blind_auction:
#     if highest_bid < blind_auction[key]:
#         highest_bid = blind_auction[key]
#         winner = key

#The above code can be minimized
winner = max(blind_auction, key = blind_auction.get)

print(f"The winner is: {winner}\nThe bid was of ${blind_auction[winner]}.")