from art import logo


print(logo)

bid_dict = {}
bidding_finished = False

while not bidding_finished:
    name = input("What is your name?\n")
    bid = int(input("What is your bid price?\n$"))

    bid_dict[name] = bid

    other_bidders = input("Are there any other bidders? type 'yes' or 'no'\n")

    if other_bidders == "no":
        bidding_finished = True
        highest_bid = 0
        winner = ""
        for key in bid_dict:
            if bid_dict[key] > highest_bid:
                highest_bid = bid_dict[key]
                winner = key
        print(f"The highest bidder was {winner} with a bid of ${highest_bid}")
