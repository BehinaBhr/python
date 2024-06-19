from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "blue", "purple"]
START_STEP = 5
INCREMENT_STEP = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()
        self.car_speed = START_STEP

    def create_car(self):
        # create less car
        chance = random.randint(1, 6)
        if chance == 6:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            rand_color = random.choice(COLORS)
            new_car.color(rand_color)
            new_car.penup()
            rand_start_y = random.randrange(-250, 250)
            new_car.goto((300, rand_start_y))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += INCREMENT_STEP
