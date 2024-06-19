from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def star_timer():
    global reps
    reps += 1
    # if it's 2nd/4th/6th rep:
    if reps % 2 == 0:
        count_down (SHORT_BREAK_MIN*60)
        label.config(text="Break", fg=RED)
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        label.config(text="Rest", fg=PINK)
    # If it's the 1st/3rd/5th/7th rep:
    else:
        count_down(WORK_MIN * 60)
        label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    if count_min < 10:
        count_min = f"0{count_min}"
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
        
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        star_timer()
        part = math.floor(reps/2)
        for n in range(part):
            check_marks.config(text="✔")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
my_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=my_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 55, "normal"))
label.grid(column=1, row=0)
check_marks = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold"))
check_marks.grid(column=1, row=3)

start_button = Button(text="Start", highlightbackground=YELLOW, command=star_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(column=2, row=2)


window.mainloop()
