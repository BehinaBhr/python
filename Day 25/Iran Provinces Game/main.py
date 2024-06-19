from turtle import Turtle, Screen
import pandas

screen = Screen()
turtle = Turtle()
screen.title("Iran Province Game")
image = "Iran_map.gif"
screen.addshape(image)
screen.bgpic(image)

data = pandas.read_csv("31_provinces.csv")
all_provinces_list = data.province.to_list()
correct_answers = []

while len(correct_answers) < 31:
    guess_answer = screen.textinput(title=f"{len(correct_answers)}/31 Provinces Correct",
                                    prompt="What's another province's name?").title()
    if guess_answer == "Exit":
        missing_provinces = []
        for province in all_provinces_list:
            if province not in correct_answers:
                missing_provinces.append(province)
        new_data = pandas.DataFrame(missing_provinces)
        new_data.to_csv("provinces_to_learn.csv")
        break
    if guess_answer in all_provinces_list and guess_answer not in correct_answers:
        correct_answers.append(guess_answer)
        turtle.hideturtle()
        turtle.penup()
        the_row = data[data.province == guess_answer]
        the_x = int(the_row.x)
        the_y = int(the_row.y)
        turtle.goto(the_x, the_y)
        turtle.color("purple")
        turtle.write(guess_answer)
