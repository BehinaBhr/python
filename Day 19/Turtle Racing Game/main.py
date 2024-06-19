from turtle import Turtle, Screen
import random

start_race = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
racers = []

for n in range(6):
    racer = Turtle(shape="turtle")
    racer.color(colors[n])
    racer.penup()
    racer.goto(-230, -150 + (n * 50))
    racers.append(racer)

if user_bet:
    start_race = True

# while start_race:
#     for racer in racers:
#         step = random.randint(2, 12)
#         racer.forward(step)
#         if racer.xcor() > 230:
#             start_race = False
#             winner = racer.pencolor()
#             if user_bet == winner:
#                 print(f"@@ You win @@ The {winner} turtle is the fastest.")
#             else:
#                 print(f"!! You lose !! The {winner} turtle is the fastest.")



## why it can not stop when ane of them win?


while start_race:

    for racer in racers:
        racer.speed(random.randint(0, 10))
        racer.forward(20)
        if racer.xcor() > 150:
            start_race = False
            winner = racer.pencolor()
            if user_bet == winner:
                print(f"@@ You win @@ The {winner} turtle is the fastest.")
            else:
                print(f"!! You lose !! The {winner} turtle is the fastest.")



screen.exitonclick()