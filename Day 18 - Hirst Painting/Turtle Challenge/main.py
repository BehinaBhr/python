from turtle import Turtle, Screen
import random
lucky = Turtle()
lucky.shape("turtle")
lucky.color("dark olive green")

# TODO: Draw a square
# for side in range(4):
#     lucky.forward(200)
#     lucky.left(90)

# TODO: Draw a dashed line
# for line in range(18):
#     lucky.pendown()
#     lucky.forward(10)
#     lucky.penup()
#     lucky.forward(5)


# TODO: Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, and decagon (360/sides = angel degree)
#  So, from 3 to 10-sided shape with a random color, each sides = 100
#  All of theme shapes overlaid on each other and drawn out in sequence.

# colors = ['orange', 'yellow', 'red', 'blue', 'black', 'purple', 'khaki', 'gray', 'pink', 'green']
# num_side = 3
# while num_side <= 10:
#     chosen_color = random.choice(colors)
#     colors.remove(chosen_color)
#     lucky.pencolor(chosen_color)
#     for side in range(num_side):
#         degree_angle = 360 / num_side
#         lucky.right(degree_angle)
#         lucky.forward(100)
#     num_side += 1

# Better way:
# colors = ['orange', 'yellow', 'red', 'blue', 'black', 'purple', 'khaki', 'brown', 'pink', 'green']
# def drawing(num_side):
#     while num_side <= 10:
#         color(colors)
#         for side in range(num_side):
#             degree_angle = 360 / num_side
#             lucky.right(degree_angle)
#             lucky.forward(100)
#         num_side += 1
#
# def color(colors):
#     chosen_color = random.choice(colors)
#     colors.remove(chosen_color)
#     lucky.pencolor(chosen_color)
#
# drawing(3)


# TODO: random walk with random color, speed, thickness

## changing color from a list:
# colors = ['orange', 'yellow', 'red', 'blue', 'black', 'purple', 'khaki', 'brown', 'pink', 'green']
#
#
# def change_color(colors):
#     chosen_color = random.choice(colors)
#     return chosen_color
#
#
# def rand_walk():
#     for walk in range(200):
#         # color(colors)
#         chosen_color = change_color()
#         lucky.pencolor(chosen_color)
#         lucky.speed(random.randint(0, 10))
#         lucky.pensize(random.randint(1, 15))
#         rand_steps = random.randint(1, 50)
#         lucky.forward(rand_steps)
#         rand_angle = random.randrange(0, 360, 90)
#         lucky.left(rand_angle)
#
#
# rand_walk()
#
# screen = Screen()
# screen.exitonclick()



## random changing color_ way 1:
# from turtle import Turtle, Screen
# import random
# lucky = Turtle()
# lucky.shape("turtle")
# lucky.color("dark olive green")
#
# screen = Screen()
# screen.colormode(255)
#
#
# def change_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     chosen_color = (r, g, b)
#     return chosen_color
#
#
# def rand_walk():
#     for walk in range(200):
#         chosen_color = change_color()
#         lucky.pencolor(chosen_color)
#         lucky.speed(random.randint(0, 10))
#         lucky.pensize(random.randint(1, 15))
#         rand_steps = random.randint(1, 50)
#         lucky.forward(rand_steps)
#         rand_angle = random.randrange(0, 360, 90)
#         lucky.left(rand_angle)
#
#
# rand_walk()
#
# screen.exitonclick()


## random changing color_ WAY 2:
# import turtle as t
# import random
# lucky = t.Turtle()
# lucky.shape("turtle")
# lucky.color("dark olive green")
#
#
# def change_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     chosen_color = (r, g, b)
#     return chosen_color
#
#
# def rand_walk():
#     for walk in range(200):
#         chosen_color = change_color()
#         lucky.pencolor(chosen_color)
#         lucky.speed(random.randint(0, 10))
#         lucky.pensize(random.randint(1, 15))
#         rand_steps = random.randint(1, 50)
#         lucky.forward(rand_steps)
#         rand_angle = random.randrange(0, 360, 90)
#         lucky.left(rand_angle)
#
#
# rand_walk()
#
# screen = t.Screen()
# screen.exitonclick()

# TODO: make a spirograph(circle)
# screen = Screen()
# screen.colormode(255)
#
#
# def change_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     chosen_color = (r, g, b)
#     return chosen_color
#
# lucky.speed("fastest")
#
# # ## Way 1:
# # def spiroghaph(gap):
# #     for _ in range(0, 360, gap):
# #         chosen_color = change_color()
# #         lucky.pencolor(chosen_color)
# #         lucky.circle(100)
# #         lucky.left(gap)
#
#
# ## Way 2:
# # def spiroghaph(gap):
# #     for _ in range(int(360/gap)):
# #         chosen_color = change_color()
# #         lucky.pencolor(chosen_color)
# #         lucky.circle(100)
# #         lucky.left(gap)
#
#
# spiroghaph(10)
# screen.exitonclick()


