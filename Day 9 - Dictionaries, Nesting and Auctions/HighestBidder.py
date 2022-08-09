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
  