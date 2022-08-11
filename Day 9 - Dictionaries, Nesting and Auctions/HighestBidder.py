from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)

dict ={}
bidding_finished = False

while not bidding_finished:
  dict_name = str(input("Enter your name: \n")).lower()
  bid_value = int(input("Enter your bid value: \n"))
  dict[dict_name] = bid_value

  question = input("Do we have another bidder? Type 'yes' or 'no'")
  if question == 'yes':
    clear()
   
  elif question == 'no':
    bidding_finished = True

# highest_bidder = "Ammar1"
# print(f"The highest bidder is {highest_bidder}")
  from replit import clear
from art import logo
print(logo)

# bids = {}
# bidding_finished = False

# def find_highest_bidder(bidding_record):
#   highest_bid = 0
#   winner = ""
#   # bidding_record = {"Angela": 123, "James": 321}
#   for bidder in bidding_record:
#     bid_amount = bidding_record[bidder]
#     if bid_amount > highest_bid: 
#       highest_bid = bid_amount
#       winner = bidder
#   print(f"The winner is {winner} with a bid of ${highest_bid}")

# while not bidding_finished:
#   name = input("What is your name?: ")
#   price = int(input("What is your bid?: $"))
#   bids[name] = price
#   should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
#   if should_continue == "no":
#     bidding_finished = True
#     find_highest_bidder(bids)
#   elif should_continue == "yes":
#     clear()
  