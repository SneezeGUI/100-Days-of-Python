from turtle import Turtle
player_1_score = 0
player_2_score = 0
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        global player_1_score
        global player_2_score
        self.speed(0)
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.write(f"Player 1: {player_1_score}                           Player 2: {player_2_score}", move=False, align="center", font=("Arial", 15, "bold"))
    ##Player 1 Scores ##
    def player_1_scores(self):
        global player_1_score
        global player_2_score
        player_1_score += 1
        self.clear()
        self.write(f"Player 1: {player_1_score}                           Player 2: {player_2_score}", move=False, align="center", font=("Arial", 15, "bold"))
        ##Player 2 Scores ##
    def player_2_scores(self):
        global player_1_score
        global player_2_score
        player_2_score += 1
        self.clear()
        self.write(f"Player 1: {player_1_score}                           Player 2: {player_2_score}", move=False, align="center", font=("Arial", 15, "bold"))
    ## Game Over##
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", move=False, align="center", font=("Arial", 25, "bold"))
        # self.goto(0,-30)
        # self.write("Play Again? (Y/N)", move=False, align="center", font=("Arial", 15, "normal"))