rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

#Write your code below this line 👇
import random
comp = random.randint(0,2)
print(comp)
you = int(input("What do you choose? type 0 for Rock, 1 for Paper, 2 for Scissors."))

# if comp == 0:
#   print(rock)
# elif comp == 1:
#   print(paper)
# else:
#   print(scissors)   
# print("computer chose")

# if you == 0:
#   print(rock)
# elif you == 1:
#   print(paper)
# elif you == 2:
#   print(scissors) 
# else:
#   print("XXXXXXX\n")
# print("Your chose") 
if you > 2 or you < 0:
  print("Invalid Input!!!!\n") 
else:
  image = [rock, paper, scissors]
  print(image[comp])
  print("Computer chose") 
  print(image[you])
  print("Your chose\n") 



if comp == you:
  victor = "No One"

if comp > you:
  if comp - you == 2:
    victor = "You"
  elif comp - you == 1:
    victor = "Computer"
  else:
    victor = "XXX"

if comp < you:
  if you - comp == 2:
    victor = "Computer"
  elif you - comp == 1:
    victor = "You"
  else:
    victor = "XXX"
    
print(f"result = {victor} win the game!")