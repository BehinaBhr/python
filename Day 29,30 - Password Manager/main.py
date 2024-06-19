# TODO: by clicking add_button, Write to the data inside the entries to a data.txt file with
#  save funtion. put all entries with a space in between and a pipe| symbol. Each time should be on a new line.
#   All fields need to be cleared after that.
# TODO: make pop up to give feedback
# TODO: Do not save the data and show the pop up above if the website or password fields were left

from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '@', "-", '_', '^']
    num_letters = random.randint(8, 10)
    num_symbols = random.randint(2, 4)
    num_numbers = random.randint(2, 4)

    pass_letters = [random.choice(letters) for _ in range(num_letters)]
    pass_numbers = [random.choice(numbers) for _ in range(num_numbers)]
    pass_symbols = [random.choice(symbols) for _ in range(num_symbols)]
    pass_char_list = pass_letters + pass_numbers + pass_symbols
    random.shuffle(pass_char_list)
    gen_pass = "".join(pass_char_list)
    pass_entry.insert(0, f"{gen_pass}")
    pyperclip.copy(gen_pass)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web_output = web_entry.get()
    email_output = email_entry.get()
    pass_output = pass_entry.get()
    new_data = {
        web_output: {
            "email": email_output,
            "password": pass_output
        }
    }

    if len(web_output) == 0 or len(email_output) == 0 or len(pass_output) == 0:
        messagebox.showinfo(title="Oops!", message="Please don't leave any field empty.")
    # else:
    #     is_ok = messagebox.askokcancel(title="Save Info",
    #                                    message="Are you sure that you want to save the details entered?")
    #     if is_ok:
    #         with open("data.txt", mode="a") as data_file:
    #             data_file.write(f"{web_output} | {email_output} | {pass_output}\n")
    #             web_entry.delete(0, END)
    #             pass_entry.delete(0, END)

    #### Day 30 ####
    # TODO: Create a new data. json file if it does not exist. If the file already exists, then simply add the new entry.

    else:
        try:
            # read old data
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except:
            # if there is no old data, write it as a new data
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # update old data with new data
            data.update(new_data)
            # save updated data
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            web_entry.delete(0, END)
            pass_entry.delete(0, END)


# ---------------------------- Search  ------------------------------- #
def search():
    web_output = web_entry.get()

    try:
        # read old data
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except:
        messagebox.showinfo(title="Error", message="No Data File Found!")

    else:
        if web_output in data:
            messagebox.showinfo(title=f"{web_output}", message=f"Email: {data[web_output]["email"]}\nPassword: {data[web_output]["password"]}")
        else:
            if web_output not in data:
                messagebox.showinfo(title="Not Found", message=f"Nothing saved before for {web_output}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
my_photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=my_photo)
canvas.grid(row=0, column=1)

web_label = Label(text="Website:")
web_label.grid(row=1, column=0)
user_label = Label(text="Email/Username:")
user_label.grid(row=2, column=0)
pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)

web_entry = Entry(width=35)
web_entry.grid(row=1, column=1, sticky=EW)
web_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky=EW)
email_entry.insert(0, "be.bhr77@gmail.com")

pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1, sticky=EW)

gen_button = Button(text="Generate Password", command=generator)
gen_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky=EW)
search_button = Button(text="Search", command=search)
search_button.grid(row=1, column=2, sticky=EW)


window.mainloop()
