# with open("./weather_data.csv") as data_file:
#     list = data_file.readlines()
#     print(list)

# import csv
# with open("./weather_data.csv") as data_file:
#     data_list = csv.reader(data_file)
#     print(data_list)
#     temperatures = []
#     for row in data_list:
#         print(row)
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# import pandas
# data = pandas.read_csv("weather_data.csv")
# print(data)
# temperatures = data["temp"]
# # Another way to get data in column:
# temperatures = data.temp
# print(temperatures)

# # DataFrame
# print(type(data))
# data_dict = data.to_dict()
# print(data_dict)

# # Series
# print(type(temperatures))
# temp_list = temperatures.to_list()
# print(temp_list)

# # average temperatures:
# total_temps = 0
# for temp in temp_list:
#     total_temps += temp
# print(total_temps/len(temp_list))
# print(sum(temp_list) / len(temp_list))
# print(temperatures.mean())

# # # get data in column:
# print(data["condition"])
# print(data.condition)

# # # get data in row:
# print(data[data.day == "Monday"])
# print(data[data["day"] == "Monday"])


# # pull out the row of data where the temperatures was at the maximum
# max_temp = data["temp"].max()
# print(data[data["temp"] == max_temp])
# # or
# max_temp = data.temp.max()
# print(data[data.temp == max_temp])


# # # get particular data in row:
# monday_row = data[data.day == "Monday"]
# print(monday_row["temp"])
# print(monday_row.temp)
# # convert temperature of monday_row to Fahrenheit
# monday_temp = monday_row.temp[0]
# print(monday_temp * 9/5 + 32)

# create a DataFrame from scratch
# data_dict = {"students": ["Amy", "James", "Angela"], "scores": [76, 56, 65]}
# new_data = pandas.DataFrame(data_dict)
# new_data.to_csv("new_data.csv")

# Squirrel
import pandas
data = pandas.read_csv("Squirrel_Data.csv")
# colors_list = data["Primary Fur Color"].to_list()
# print(colors_list)
# num_gray = 0
# num_black = 0
# num_cinnamon = 0
# for color in colors_list:
#     if color == "Gray":
#         num_gray += 1
#     elif color == "Black":
#         num_black += 1
#     elif color == "Cinnamon":
#         num_cinnamon += 1
#
# print(num_gray)
# print(num_black)
# print(num_cinnamon)

# Another way:
grey_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_count)
print(red_count)
print(black_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_count, red_count, black_count]
}

New_Squirrel_Data = pandas.DataFrame(data_dict)
New_Squirrel_Data.to_csv("New_Squirrel_Data.csv")


