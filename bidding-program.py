from bidding_program_art import logo
from replit import clear

print(logo)

bids = {}
done_bidding = False

def highest_bidder(record):  # A function to find the highest bidder
    highest = 0  # Will keep track on who has the highest bid
    for person in record:  # Looping on each person
        total_bid = record[person]  # Getting the Value using the Key
        if total_bid > highest:
            highest = total_bid
            winner = person
    print(f"\nThe winner is {winner} with a bid of ${highest}.")



while not done_bidding:
    name = input("Enter your name: ")
    bid = int(input("Enter your bid: $"))
    bids[name] = bid
    choice = input("Are there any other bidders? Y for yes, N for no: ")
    if choice == "N":
        done_bidding = True
        highest_bidder(bids)
    elif choice == "Y":
        clear()
