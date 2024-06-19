from tkinter import *


window = Tk()
window.title("Mile to Km Convertor")
window.minsize(width=60, height=80)
window.config(padx=10, pady=10)

# label
label_mile = Label(text="Miles")
label_mile.grid(row=0, column=2)

label_equal = Label(text="is equal to")
label_equal.grid(row=1, column=0)

label_result = Label(text="0")
label_result.grid(row=1, column=1)


label_km = Label(text="Km")
label_km.grid(row=1, column=2)

# Entry
entry = Entry(width=10)
entry.grid(row=0, column=1)


# Button
def action():
    result = float(entry.get()) * 1.6
    label_result.config(text=f"{round(result, 3)}")


button = Button(text="Calculate", command=action)
button.grid(row=2, column=1)




window.mainloop()
