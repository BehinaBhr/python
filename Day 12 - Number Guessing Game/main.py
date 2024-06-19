#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
NUMBERS = []
for n in range(1,101):
    NUMBERS.append(n)
ANSWER = random.choice(NUMBERS)
print(f"Hint: the correct answer is {ANSWER}") 

def compare(guess):
    if guess < ANSWER:
        print("Too low!")
    elif guess > ANSWER:
        print("Too high!")
    elif guess == ANSWER:
        print(f"*** You got it! The answer was {ANSWER}. ***")
        
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if level == "easy":
    remain_attempts = 10
    for _ in range(10): 
        print(f"You have {remain_attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        remain_attempts -= 1
        compare(guess)
        if remain_attempts == 0:
            print("@ you lose! You've run out of guesses. @")
    
        
elif level == "hard":
    remain_attempts = 5
    for _ in range(5):
        print(f"You have {remain_attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        remain_attempts -= 1
        compare(guess)
        if remain_attempts == 0:
            print("@ you lose! You've run out of guesses. @")
    