import turtle
from turtle import Turtle
ALIGN = 'center'
FONT = ('Arial', 12, 'bold')
GAME_OVER_FONT = ('Arial', 24, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.new_scoreboard()

    def new_scoreboard(self):
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGN, font=FONT)

    def new_score(self):
        self.clear()
        self.score += 1
        self.new_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGN, font=GAME_OVER_FONT)
        self.goto(0, -30)
        self.write(f"Final score: {self.score}", align=ALIGN, font=FONT)
        self.goto(0, -90)
        self.write("Press Space to play again.", align=ALIGN, font=FONT)

    def highest_score(self):
        self.goto(0, -60)
        if self.score > self.high_score:
            self.high_score = self.score
            self.write(f"New highest score: {self.high_score}", align=ALIGN, font=FONT)
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        else:
            self.write(f"Highest score: {self.high_score}", align=ALIGN, font=FONT)
