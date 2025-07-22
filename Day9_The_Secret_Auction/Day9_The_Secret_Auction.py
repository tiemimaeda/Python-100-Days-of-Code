import secretauctionlogo

print(secretauctionlogo.logo)

def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_ammount = bidding_dictionary[bidder]
        if bid_ammount > highest_bid:
            highest_bid = bid_ammount
            winner = bidder
    
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

bids = {}
continue_bidding = True

while continue_bidding:
    user_name = input("What is your name? ")
    user_price = int(input("What is your bid? $"))

    bids[user_name] = user_price

    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)
