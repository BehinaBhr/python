from turtle import Turtle

SNAKE_PART = 3
STEP = 20


class Snake:
    def __init__(self):
        self.total_parts = []
        self.create_snake()
        self.head = self.total_parts[0]
        self.tail = self.total_parts[-1]

    def create_snake(self):
        # for n in range(SNAKE_PART):
        #     new_part = Turtle("square")
        #     new_part.color("white")
        #     new_part.penup()
        #     new_part.goto(-20 * n, 0)
        #     self.total_parts.append(new_part)
        ## Another way:
        for n in range(SNAKE_PART):
            self.add_new_part((-20 * n, 0))

    def add_new_part(self, position):
        new_part = Turtle("square")
        new_part.color("white")
        new_part.penup()
        new_part.goto(position)
        self.total_parts.append(new_part)

    def extend(self):
        self.add_new_part(self.tail.position())

    def move_snake(self):
        # 3_part_snake position = 2, 1, 0
        for index_part in range(len(self.total_parts) - 1, 0, -1):
            new_x = self.total_parts[index_part - 1].xcor()
            new_y = self.total_parts[index_part - 1].ycor()
            self.total_parts[index_part].goto(new_x, new_y)

        self.head.forward(STEP)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def reset(self):
        # get rid of the dead body in screen
        for part in self.total_parts:
            part.goto(1000, 1000)
        # do all in init again
        self.total_parts.clear()
        self.create_snake()
        self.head = self.total_parts[0]
