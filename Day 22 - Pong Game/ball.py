from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_b_x = self.xcor() + self.x_move
        new_b_y = self.ycor() + self.y_move
        self.goto(new_b_x, new_b_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def inverse_move(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()

    # def move_faster(self):
    #     self.x_move += 5
    #     self.y_move += 5
