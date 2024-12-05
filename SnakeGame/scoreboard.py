from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        with open(f"highscore.txt", mode="r") as file:
            self.highscore = int(file.read())

        self.speed(0)
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.write(f"Score: {self.score}    Highscore: {self.highscore}", move=False, align="center", font=("Arial", 12, "bold"))
    ##Score UP##
    def score_refresh(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}    Highscore: {self.highscore}", move=False, align="center", font=("Arial", 12, "bold"))


    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", mode="w") as file:
                file.write(f"{self.highscore}")
            self.clear()
            self.write(f"Score: {self.score}    Highscore: {self.highscore}", move=False, align="center", font=("Arial", 12, "bold"))
        self.score = 0
    ## Game Over##
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", move=False, align="center", font=("Arial", 25, "bold"))
    #     # self.goto(0,-30)
    #     # self.write("Play Again? (Y/N)", move=False, align="center", font=("Arial", 15, "normal"))