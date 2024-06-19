from turtle import Turtle

START_POS = (0, -280)
STEP = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.speed("fastest")
        self.left(90)
        # self.setheading(90)
        self.go_to_start()

    def go_up(self):
        p_y = self.ycor() + STEP
        self.goto(0, p_y)

    def go_to_start(self):
        self.goto(START_POS)

    def cross_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
