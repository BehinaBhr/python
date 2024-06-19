# TODO: Create two new methods that work as a command to the buttons.
#  by calling check_answer() from the quiz_brain and pass over "True" or "False" as user_answer.

# TODO: Change the canvas' background colour to green if is_right_answer is True
#  and change it to red if is_right_answer is False.
# TODO: When a button has been pressed, display the next question after 1000 milliseconds,
#  but make sure to change the background back to white.

from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        yes_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=yes_image, bd=0, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)

        no_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=no_image, bd=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas_text = self.canvas.create_text(150, 125, width=280,
                                                   text="Question Text", fill="black", font=FONT)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions() == True:
            updated_score = self.quiz.score
            self.score_label.config(text=f"SCORE: {updated_score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text="The END.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_right_answer = self.quiz.check_answer("True")
        self.give_feedback(is_right_answer)

    def false_pressed(self):
        is_right_answer = self.quiz.check_answer("False")
        self.give_feedback(is_right_answer)

    def give_feedback(self, is_right_answer):
        if is_right_answer == True:
            self.canvas.config(bg="green")
            self.window.after(1000, self.get_next_question)

        if is_right_answer == False:
            self.canvas.config(bg="red")
            self.window.after(1000, self.get_next_question)
