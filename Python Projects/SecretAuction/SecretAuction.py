import os

#Auction Logo
from art import logo
print(logo)

#Empty Dictionary to store bid and name
bids = {}
bidding_done = False

#Function To calculate maximum bid amount
def max_bid(record):
    high_bid = 0
    winner = ""
    for bidder in record:
        price = record[bidder]
        if price > high_bid:
            high_bid = price
            winner = bidder
    print(f"The winner is {winner} with a bid amount of Rs.{high_bid}")


while not bidding_done:
    name = input("What is your name?:  ")
    amount = int(input("What is your bid amount? Rs."))

    bids[name] = amount 

    going = input("Are there more bidders? Type 'yes' or 'no'.\n")
    if going == "no":
        bidding_done = True
        max_bid(bids)
    elif going == "yes":
        os.system('cls')