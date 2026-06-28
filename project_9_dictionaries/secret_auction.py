from art import gavel
from os import system

bidders = {}

print(gavel)


def input_bid():
    name = input("What is your name? ")
    bid = int(input("What is your bid? £"))
    bidders[name] = bid

    more = input("Are there any more bidders? Type 'yes' or 'no'. \n")

    if more == 'yes':
        next_bid()
    else:
        show_highest_bidder()


def next_bid():
    system("clear")
    input_bid()

def show_highest_bidder():
    system("clear")
    highest_bidder = ''
    highest_bid = 0
    for bidder, bid in bidders.items():
        if bid > highest_bid:
            highest_bid = bid
            highest_bidder = bidder
    

    print(f'The highest bidder is {highest_bidder} with a bid of £{highest_bid}')

print('Welcome to the secret auction program.')
input_bid()
