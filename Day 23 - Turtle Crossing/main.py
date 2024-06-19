# TODO:  create a Turtle screen 600 * 600px,
#  turn off tracer(0) and use update() to refresh the screen every 0.1s by importing time
# TODO: player moves forwards when you press the "Up" key
# TODO: Cars are randomly along the y-axis move from right edge to left
# TODO: move turtle with key
# TODO: create and move cars
# TODO: detect collision with car
# TODO: detect collision with finish line
# TODO: create a scoreboard for level

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from turtle import Screen
import time


player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen = Screen()
screen.bgcolor("white")
screen.screensize(600, 600)
screen.title("Turtle Crossing Capstone")

screen.tracer(0)

screen.listen()
screen.onkey(player.go_up, "Up")


start = True
while start:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    # detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            start = False
            scoreboard.game_over()
    # detect collision with final line
    if player.cross_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.next_level()




screen.exitonclick()

