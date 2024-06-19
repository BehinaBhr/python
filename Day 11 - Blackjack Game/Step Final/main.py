from art import logo
from replit import clear
import random


def calculate(turn):
    turn.append(random.choice(cards))
    turn.append(random.choice(cards))
    score = turn[0] + turn[1]
    
    if score == 21 and len(turn) == 2 :
        return 0
    elif score > 21 and 11 in turn:
        turn.remove(11)
        turn.append(1)
        
    return score
    
def compare(yours_score, comp_score):
    if yours_score == comp_score:
        print("Draw!")
    elif comp_score == 0:
        print("You lose! Computer has Blakcjak")
    elif yours_score == 0:
        print("!! You Win with Blakcjak !!")
    elif yours_score > 21:   
        print("You lose! You went over")
    elif comp_score > 21:
        print("!! You Win Computer went over !!")
    elif yours_score > comp_score:
        print("!! You win !!")
    # elif yours_score < comp_score: 
    else:
        print("You lose!")
        
    


cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
play_again = True

while play_again:
    clear()
    print("Let's play!")
    print(logo)
    yours = []
    comp = []
    end_game = False
    yours_score = calculate(yours)
    comp_score = calculate(comp) 
    # print(comp)
    while not end_game:
        print(f"Your cards: {yours}, current score: {yours_score}")
        print(f"Computer's first card: {comp[0]}")
        
        if yours_score == 0 or comp_score == 0 or yours_score > 21:
            end_game = True 
        else:
            new = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if new == "y":
                yours_new = random.choice(cards)
                yours.append(yours_new)
                yours_score += yours_new
            elif new == "n":
                end_game = True
                while comp_score != 0 and comp_score < 17:
                    comp_new = random.choice(cards)
                    comp.append(comp_new)
                    comp_score += comp_new
    print(f"Your final cards: {yours}, final score: {yours_score}")        
    print(f"Computer's final card: {comp} final score: {comp_score}")
    print("result...")
    compare(yours_score, comp_score)
    play = input("Do you want to play again? Type 'y' or 'n': ").lower()
    if play == 'n':
        play_again = False
        print("Goodbye!")
        
    
    
