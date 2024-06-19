from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 22, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # self.high_score = 0
        # saving high scores into a file and retrieve it the next time we open up our program.
        with open("data.txt") as data:
            self.high_score = int(data.read())

        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score}   High_score: {self.high_score}", align=ALIGN,  font=FONT)

    def get_score(self):
        self.score += 1
        self.display_score()

    def replay(self):
        if self.score >= self.high_score:
            self.high_score = self.score
            # saving high scores into a file and retrieve it the next time we open up our program.
            with open("data.text", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.display_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("!! Game over !!", align=ALIGN,  font=FONT)
