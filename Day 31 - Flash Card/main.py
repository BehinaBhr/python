# TODO: window 526 * 800 with 50 pading, 2 X 2 grid.
# TODO: The flash card is a Canvas with 1 image card_front.png and 2 pieces of text
#  (400,150), (400,263) font(Ariel,40, italic), (Ariel, 60, bold).
# TODO: Use the images,create The ❌ and ✅ are buttons by adding images to buttons
# TODO: Read the data from the french_words.csv Pick a random French word/translation
# TODO: pandas to access the CSV and generate a data frame of all the rows out
#  as a list of dictionaries [{french_word: english_word}]
# TODO: Every time you press the ❌ or ✅ buttons, it should generate a new random word to display.
# TODO: After a delay of 3s (3000ms), the card should flip and display the English translation.
# TODO: The canvas image change to the card_back.png and the text colour change to white(fill="white").
#  The title of the card should change to "English" from "French".
# TODO: When they press ✅ remove the word from the list of words that might come up.
# TODO: saved the updated data to a new file called words_to_learn.csv
# TODO: next time check if there is a words_to_learn.csv file.
#  If it exists, the program should use those words
#  If it does not exist (the first time ), then it should use the words in the french_words.csv


# # # # # # flash card without flipping # # # # # #
# from tkinter import *
# import pandas
# import random
#
# BG_COLOR = "#B1DDC6"
# FONT_W = ("Arial", 40, "italic")
# FONT_M = ("Ariel", 60, "bold")
#
#
# window = Tk()
# window.title("Flashy")
# window.config(padx=50, pady=50, bg=BG_COLOR)
#
# data = pandas.read_csv("data/french_words.csv")
# dict = {row.French: row.English for (index, row) in data.iterrows()}
# word_list = [key for (key, value) in dict.items()]
# meaning_list = [value for (key, value) in dict.items()]
# canvas = Canvas(width=800, height=526, bg=BG_COLOR, highlightthickness=0)
# my_photo = PhotoImage(file="images/card_front.png")
# canvas.create_image(410, 280, image=my_photo)
# canvas.create_text(400, 150, text=f"{random.choice(word_list)}", font=FONT_W)
# canvas.create_text(400, 263, text=f"{random.choice(meaning_list)}", font=FONT_M)
# canvas.grid(row=0, column=0, columnspan=2)

# # another way:
# dict = data.to_dict(orient='records')
# turn = random.choice(dict)
# canvas = Canvas(width=800, height=526, bg=BG_COLOR, highlightthickness=0)
# my_photo = PhotoImage(file="images/card_front.png")
# canvas.create_image(410, 280, image=my_photo)
# first_title = canvas.create_text(400, 150, text=f"{turn["French"]}", font=FONT_W)
# second_title = canvas.create_text(400, 263, text=f"{turn["English"]}", font=FONT_M)
# canvas.grid(row=0, column=0, columnspan=2)
#
#
# def next_card():
#     new_turn = random.choice(dict)
#     canvas.itemconfig(first_title, text=f"{new_turn["French"]}")
#     canvas.itemconfig(second_title, text=f"{new_turn["English"]}")

# wrong_img = PhotoImage(file="images/wrong.png")
# wrong_button = Button(image=wrong_img, highlightbackground=BG_COLOR, command=next_card)
# wrong_button.grid(row=1, column=0)
# right_img = PhotoImage(file="images/right.png")
# right_button = Button(image=right_img, highlightbackground=BG_COLOR, command=next_card)
# right_button.grid(row=1, column=1)
#
# window.mainloop()


# # # # # # flash card with flipping # # # # # #
from tkinter import *
import pandas
import random

BG_COLOR = "#B1DDC6"
FONT_W = ("Arial", 40, "italic")
FONT_M = ("Ariel", 60, "bold")
# turn = {}
# dict_vocabs = {}

def flip_card():
    canvas.itemconfig(card_image, image=back_photo)
    canvas.itemconfig(first_title, text="English", fill="white")
    canvas.itemconfig(second_title, text=f"{turn["English"]}", fill="white")


def next_card():
    global turn, flip_timer
    window.after_cancel(flip_timer)
    turn = random.choice(dict_vocabs)
    canvas.itemconfig(card_image, image=front_photo)
    canvas.itemconfig(first_title, text="French", fill="black")
    canvas.itemconfig(second_title, text=f"{turn["French"]}", fill="black")
    flip_timer = window.after(3000, flip_card)


def is_known():
    global turn, dict_vocabs
    dict_vocabs.remove(turn)
    new_data = pandas.DataFrame(dict_vocabs)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BG_COLOR)
flip_timer = window.after(3000, flip_card)

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except:
    data = pandas.read_csv("data/french_words.csv")
finally:
    dict_vocabs = data.to_dict(orient='records')

turn = random.choice(dict_vocabs)
canvas = Canvas(width=800, height=526, bg=BG_COLOR, highlightthickness=0)
front_photo = PhotoImage(file="images/card_front.png")
back_photo = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(410, 280, image=front_photo)
first_title = canvas.create_text(400, 150, text="French", fill="black",  font=FONT_W)
second_title = canvas.create_text(400, 263, text=f"{turn["French"]}",  fill="black", font=FONT_M)
canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightbackground=BG_COLOR, command=next_card)
wrong_button.grid(row=1, column=0)
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightbackground=BG_COLOR, command=is_known)
right_button.grid(row=1, column=1)

window.mainloop()
