from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.r_score = 0
        self.l_score = 0
        self.display()

    def display(self):
        self.clear()
        self.goto(-100, 250)
        self.write(f"Score: {self.l_score} ", align='center', font=('Arial', 24, 'normal'))
        self.goto(100, 250)
        self.write(f"Score: {self.r_score} ", align='center', font=('Arial', 24, 'normal'))

    def r_point(self):
        self.r_score += 1
        self.display()

    def l_point(self):
        self.l_score += 1
        self.display()

