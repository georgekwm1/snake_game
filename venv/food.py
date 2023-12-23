from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Move the food to a new location."""
        random_x = random.randint(-288, 288)
        random_y = random.randint(-288, 288)
        self.goto(random_x, random_y)