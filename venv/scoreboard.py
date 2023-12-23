from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.write(f"Score: {self.score}", False, align="center", font=("Arial", 12, "normal"))

    def score_increase(self):
        """Increases the player's score by one."""
        self.clear()
        self.score += 1
        self.goto(0, 280)
        self.write(f"Score: {self.score}", False, align="center", font=("Arial", 12, "normal"))
        
    
    