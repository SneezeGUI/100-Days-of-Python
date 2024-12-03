from idlelib.configdialog import font_sample_text
from tkinter.constants import CENTER
from turtle import Turtle
score = 0
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        global score
        self.speed(0)
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.write(f"Score: {score}", move=False, align="center", font=("Arial", 12, "bold"))
    ##Score UP##
    def score_refresh(self):
        global score
        score += 1
        self.clear()
        self.write(f"Score: {score}", move=False, align="center", font=("Arial", 12, "bold"))

    ## Game Over##
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", move=False, align="center", font=("Arial", 25, "bold"))
        # self.goto(0,-30)
        # self.write("Play Again? (Y/N)", move=False, align="center", font=("Arial", 15, "normal"))