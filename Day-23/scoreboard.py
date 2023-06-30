from turtle import Turtle

FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.count = 1
        self.goto(-280, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.count}", False, "left", FONT)

    def increase_level(self):
        self.count += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)



