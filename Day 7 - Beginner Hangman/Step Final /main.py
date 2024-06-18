# My Final Step

import random

# Update the word list 
from hangman_words import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# Show logo at the start of the game.
from hangman_art import logo
print(logo)

# Testing code
print(f'Hint: the solution is {chosen_word}.')

# Create blanks
display = ["_" for _ in range(word_length)]
guessed = []


while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
# Forgive a duplicate guess
    if guess in guessed:
        print(f"You've already guessed {guess}. Try another one.")
    else:
        guessed.append(guess)

# Check guessed letter and update display
        if guess in chosen_word:
            for position in range(word_length):
                if chosen_word[position] == guess:
                    display[position] = guess
            print(f"Correct! {guess} is in the word.")
            
# Check if user is wrong.    
        # else:
        elif guess not in chosen_word:
            print(f"Wrong guess! {guess} isn't in the word so, you lose a life.")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("*** You lose :(( ***")

# Join all the elements in the list and turn it into a String.
    print(" ".join(display))

# Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("*** You win :)) ***")

# Print the current hangman stage
    from hangman_art import stages
    print(stages[lives])
