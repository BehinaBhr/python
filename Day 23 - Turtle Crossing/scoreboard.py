from turtle import Turtle

FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280,250)
        self.display()

    def display(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def next_level(self):
        self.level += 1
        self.display()

    def game_over(self):
        self.goto(0, 0)
        self.write(f" GAME OVER !!", align="center", font=FONT)