from turtle import Turtle, Screen
lucky = Turtle()

# TODO: Using screen events to listen by click
# TODO: listen by click w = forward, s = backward, a = counter-clockwise, d = clockwise,
#  c = clear drawing of this turtle and move to the first position


def move_forward():
    lucky.forward(10)


def move_backward():
    lucky.backward(10)


def move_clockwise():
    lucky.right(10)


def move_counter_clockwise():
    lucky.left(10)


def clear():
    lucky.clear()
    lucky.penup()
    lucky.speed("fast")
    lucky.home()



screen = Screen()
screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_counter_clockwise, "a")
screen.onkey(move_clockwise, "d")
screen.onkey(clear, "c")


screen.exitonclick()

