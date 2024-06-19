# TODO: create a snake body: 3 turtle(white squares 20*20)
# TODO: move the snake: move the last segment to the position of the one beside it,
#  and continue this process until the segment beside it moves to the position of the first segment
# TODO: create Snake, Food, Scoreboard class
# TODO: create snake food
# TODO: detect collision with food
# TODO: create a scoreboard
# TODO: detect collision with walls
# TODO: detect collision with tail

from snake import Snake
from food import Food
from scoreboard import Scoreboard
from turtle import Screen
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

start = True
while start:
    screen.update()
    time.sleep(0.2)
    snake.move_snake()

    # Detect collision with food(10*10)
    if snake.head.distance(food) < 15:
        food.rand_location()
        snake.extend()
        scoreboard.get_score()

    # Detect collision with walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        # start = False
        # scoreboard.game_over()
        scoreboard.replay()
        snake.reset()

    # Detect collision with snake's body except head(first part)
    for part in snake.total_parts[1:]:
        if snake.head.distance(part) < 10:
            # start = False
            # scoreboard.game_over()
            scoreboard.replay()
            snake.reset()


screen.exitonclick()
