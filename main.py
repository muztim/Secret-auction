from art import logo
print(logo)

bid_list = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record(bidder)
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

while not bidding_finished:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bid_list[name] = bid
    should_continue = input("Are there any other bidder? Type 'Yes' or No'. \n").lower()
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bid_list)
    elif should_continue == "yes":
        #clear()


print(bid_list)

# TODO: Create a clear function for Pycharm IDE: clear()

