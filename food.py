from turtle import Turtle
import random

FOOD_COLOR = ["red", "blue", "white", "pink", "yellow", "green"]

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len= 0.5, stretch_wid= 0.5) # default 20-20, now 10-10
        self.color(random.choice(FOOD_COLOR))
        self.speed("fastest")
        x_cor = random.randint(-270, 270)
        y_cor = random.randint(-270, 270)
        self.goto(x_cor, y_cor)
        #self.refresh()

    def refresh(self):
        self.color(random.choice(FOOD_COLOR))
        x_cor = random.randint(-270, 270)
        y_cor = random.randint(-270, 270)
        self.goto(x_cor, y_cor)