from art import logo
print(logo)
def find_highest_bidder(bidding_dictionary):
    highest_bid=0
    winner=""
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f"Highest bidder is {winner} with the highest bid of ₹{highest_bid}")


bids = {}
continue_bidding = True
while continue_bidding is True:
    name = input("Enter your name:")
    price = int(input("What is your bid?: ₹"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    if should_continue == "yes":
        continue_bidding=True
        print("\n" * 100)
    elif should_continue == "no":
        continue_bidding=False
        find_highest_bidder(bids)
        
