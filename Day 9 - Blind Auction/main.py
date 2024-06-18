from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
print("Welcome to the secret action program!")
play = True
dict = {}
while play is True:
    key = input("What's your name?  ")
    value = int(input("What's your bid?  "))
    dict[key] = value
    again = input("Are there any other bidder? type 'Yes' or 'No'.  ").lower()
    if again == "yes":
        play = True
        clear()
    else:
        winner_name = ""
        winner_bid = 0
        for key in dict:
            if dict[key] >= winner_bid:
                winner_bid = dict[key]
                winner_name = key
        print(f"The winner is {winner_name} with a bid of {winner_bid}.")
        play = False
            
