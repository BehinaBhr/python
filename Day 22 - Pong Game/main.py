
# TODO: create black screen 600*800
# TODO: create and move paddle + turn off animation and then update screen
# TODO: create and move another paddle
# TODO: create and move the ball
# TODO: detect collision with wall and bounce
# TODO: detect collision with paddle and bounce
# TODO: detect when paddle misses and get score

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.title("Pong Game")
screen.bgcolor("black")

# turn off animation
screen.tracer(0)

ball = Ball()
scoreboard = Scoreboard()


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

start = True
while start:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with r_paddle, l_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect when paddle misses
    if ball.xcor() > 380:
        ball.inverse_move()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.inverse_move()
        scoreboard.r_point()



screen.exitonclick()