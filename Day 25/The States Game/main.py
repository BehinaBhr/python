# TODO: convert guess answer to Title case
# ToDo: if the guess is among the 50 state write it onto map
# ToDo: use the loop to keep guessing
# ToDo: record the correct guesses in a list
# ToDo: track score in title


import pandas
from turtle import Turtle, Screen

screen = Screen()
turtle = Turtle()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
# turtle.shape(image)
screen.bgpic(image)
# # image disappear after the first guess if we use turtle.shape(image) and turtle.hideturtle()
# so instead we can use screen.bgpic(image)

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()
correct_answers = []

while len(correct_answers) < len(states_list):
    guess_answer = screen.textinput(f"{len(correct_answers)}/50 correct states",
                                    "What is another state's name?").title()

    if guess_answer == "Exit":
        # # put rest to states_to_learn.csv
        missing_states = []
        for state in states_list:
            if state not in correct_answers:
                missing_states.append(state)
        # list comprehension:
        # missing_states = [state for state in states_list if state not in correct_answers]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if guess_answer in states_list and guess_answer not in correct_answers:
        correct_answers.append(guess_answer)
        turtle.hideturtle()
        turtle.penup()
        the_row = data[data.state == guess_answer]
        the_x = int(the_row.x)
        the_y = int(the_row.y)
        turtle.goto(the_x, the_y)
        # guess_answer = the_row.state.item()
        turtle.write(guess_answer, align="center", font=("arial", 8, "normal"))

        # # another way without screen.bgpic(image)
        # t = Turtle()
        # t.hideturtle()
        # t.penup()
        # the_row = data[data.state == guess_answer]
        # the_x = int(the_row.x)
        # the_y = int(the_row.y)
        # t.goto(the_x, the_y)
        # t.write(guess_answer, align="center", font=("arial", 8, "normal"))

# # keeping our screen open even though our code has finished running an alternative to screen.exitonclick
# screen.mainloop()
# screen.exitonclick()
