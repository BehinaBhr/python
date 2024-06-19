from turtle import Turtle, Screen
import pandas
import os

screen = Screen()
turtle = Turtle()
screen.title("U.S. States Game")
image = "Iran_map.gif"
screen.addshape(image)
turtle.shape(image)

data_dict = {"province": [], "x": [], "y": []}

if os.path.exists('../31_provinces.csv'):
    previous_data = pandas.read_csv('../31_provinces.csv')
    for pre_province in previous_data["province"].to_list():
        data_dict['province'].append(pre_province)
    for pre_x in previous_data["x"].to_list():
        data_dict['x'].append(pre_x)
    for pre_y in previous_data["y"].to_list():
        data_dict['y'].append(pre_y)


def get_mouse_click_cor(x, y):
    province_name = screen.textinput("write province name", "Province name: ").title()
    print(province_name, x, y)
    data_dict["province"].append(province_name)
    data_dict["x"].append(x)
    data_dict["y"].append(y)
    data_file = pandas.DataFrame(data_dict)
    print(data_dict)
    data_file.to_csv("31_provinces.csv")


while len(data_dict["province"]) < 31:
    screen.onscreenclick(map.get_mouse_click_cor)
    screen.mainloop()
