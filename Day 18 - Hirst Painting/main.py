from turtle import Turtle, Screen
import random

# import colorgram
# rgb_colors = []
# colors = colorgram.extract("painting_image.jpg", 40)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_color = (r, g, b)
#     rgb_colors.append(rgb_color)
#
# print(rgb_colors)
colors_list =[(223, 236, 228), (236, 230, 216), (140, 176, 207), (25, 32, 48), (26, 107, 159), (237, 225, 235), (209, 161, 111), (144, 29, 63), (230, 212, 93), (4, 163, 197), (218, 60, 84), (229, 79, 43), (195, 130, 169), (54, 168, 114), (28, 61, 116), (172, 53, 95), (108, 182, 90), (110, 99, 87), (193, 187, 46), (240, 204, 2), (1, 102, 119), (19, 22, 21), (50, 150, 109), (172, 212, 172), (118, 36, 34), (221, 173, 188), (227, 174, 166), (153, 205, 220), (184, 185, 210), (77, 37, 76), (120, 117, 155), (35, 35, 35)]

# TODO: paint 10 by 10 rows of spots. Each of dots 20 in size and spaced apart by 50 paces.
lucky = Turtle()
screen = Screen()
screen.colormode(255)
draw_line = 0
lucky.hideturtle()


def go_new_line():
    lucky.speed("fastest")
    lucky.penup()
    lucky.left(90)
    lucky.forward(50)
    lucky.left(90)
    lucky.forward(500)
    lucky.left(180)


lucky.speed("normal")
while draw_line <= 10:
    for _ in range(10):
        dot_color = random.choice(colors_list)
        lucky.dot(20, dot_color)
        lucky.penup()
        lucky.forward(50)
    go_new_line()
    draw_line += 1

screen.exitonclick()