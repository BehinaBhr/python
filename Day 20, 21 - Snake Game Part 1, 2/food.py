# TODO: the food class render itself as a small circle on the screen in a random location
# TODO: when the snake collision with food, the food moves to a new random location.

from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        # self.dot(10, "blue")????
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.penup()
        self.speed("fastest")
        self.rand_location()

    def rand_location(self):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)

