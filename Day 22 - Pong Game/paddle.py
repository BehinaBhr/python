from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.penup()
        self.goto(position)

    def go_up(self):
        p_x = self.xcor()
        p_y = self.ycor() + 30
        self.goto(p_x, p_y)

    def go_down(self):
        p_x = self.xcor()
        p_y = self.ycor() - 30
        self.goto(p_x, p_y)

