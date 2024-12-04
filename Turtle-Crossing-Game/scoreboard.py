from turtle import Turtle
import time
FONT = ("Courier", 24, "normal")



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_level = 1
        self.penup()
        self.color("black")
        self.hideturtle()
        self.speed(0)
        self.goto(-260,280)
        self.write(f"Level: {self.current_level}", move=False, align="center", font=("Arial", 12, "bold"))

        # New Level
    def new_level(self):
        self.current_level += 1
        self.clear()
        self.write(f"Level: {self.current_level}", move=False, align="center", font=("Arial", 12, "bold"))

        ## Game Over##
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align="center", font=("Arial", 25, "bold"))
        # self.goto(0,-30)
        # self.write("Play Again? (Y/N)", move=False, align="center", font=("Arial", 15, "normal"))