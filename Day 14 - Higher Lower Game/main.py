# from art import logo, vs
# import random
# from game_data import data
# from replit import clear


# start = True
# score = 0
      
# while start:
    # rand_A = random.choice(data)
    # print(logo)
    # print(f"Compare A: {rand_A['name']}, {rand_A['description']}, from {rand_A['country']}.")
    # #Hint:
    # print(rand_A['follower_count'])

    
    # print(vs)
    # rand_B = random.choice(data)
    # if rand_A == rand_B:
    #     rand_B = random.choice(data)
    # print(f"Against B: {rand_B['name']}, {rand_B['description']}, from {rand_B['country']}.")
    # #Hint:
    # print(rand_B['follower_count'])
    
    # guess = input("Who has more followers? Type 'A' or 'B': ")
    # clear()
    # if rand_A['follower_count'] > rand_B['follower_count']:
    #     winner = "A"
    # elif rand_A['follower_count'] < rand_B['follower_count']:
    #     winner = "B"
    # if guess == winner:
    #     score += 1
    #     print(f"@ You're right! Current score: {score}. @")
    # elif guess != winner:
    #     score += 0
    #     print(f"@ Game Over! that's wrong. Final score:{score} @")
    #     start = False 
    
    
  
# ###### WAY 2 ######  

# from art import logo, vs
# import random
# from game_data import data
# from replit import clear


# start = True
# score = 0      
# def rand_data():
#     return random.choice(data)
    
# def rand_info(rand):
#     #hint
#     print(f"{rand['follower_count']}")
#     return f"{rand['name']}, a {rand['description']}, from {rand['country']}"

# def compare(rand_A, rand_B, guess):
#     if rand_A['follower_count'] > rand_B['follower_count']:
#         winner = "A"
#     elif rand_A['follower_count'] < rand_B['follower_count']:
#         winner = "B"
#     if guess == winner:
#         result = "win"
#     elif guess != winner:
#         result = "lose"
#     return result

# while start:
#     print(logo)
#     rand_A = rand_data()
#     print(f"Compare A: {rand_info(rand_A)}.")
    
#     print(vs)
    
#     rand_B = rand_data()
#     if rand_A == rand_B:
#         rand_B = rand_data()
#     print(f"Against B: {rand_info(rand_B)}.")
    
    
#     guess = input("Who has more followers? Type 'A' or 'B': ")
#     clear()
#     result = compare(rand_A, rand_B, guess)
#     if result == "win":
#         score += 1
#         print(f"@ You're right! Current score: {score}. @")
#     elif result == "lose":
#         print(f"@ Game Over! that's wrong. Final score:{score} @")
#         start = False



######## WAy 3: previous B becomes the new A #######
from art import logo, vs
import random
from game_data import data
from replit import clear


start = True
score = 0    


def rand_data():
    return random.choice(data)
    
def rand_info(rand):
    #hint
    print(f"{rand['follower_count']}")
    return f"{rand['name']}, a {rand['description']}, from {rand['country']}"

def compare(rand_A, rand_B, guess):
    if rand_A['follower_count'] > rand_B['follower_count']:
        winner = "A"
    elif rand_A['follower_count'] < rand_B['follower_count']:
        winner = "B"
    if guess == winner:
        result = "win"
    elif guess != winner:
        result = "lose"
    return result

rand_A = rand_data()
rand_B = rand_data()

while start:
    print(logo)
    rand_A = rand_B
    print(f"Compare A: {rand_info(rand_A)}.")
    
    print(vs)
    rand_B = rand_data()
    if rand_A == rand_B:
        rand_B = rand_data()
    print(f"Against B: {rand_info(rand_B)}.")
    
    
    guess = input("Who has more followers? Type 'A' or 'B': ")
    clear()
    result = compare(rand_A, rand_B, guess)
    if result == "win":
        score += 1
        print(f"@ You're right! Current score: {score}. @")
    elif result == "lose":
        print(f"@ Game Over! that's wrong. Final score:{score} @")
        start = False
         
        

