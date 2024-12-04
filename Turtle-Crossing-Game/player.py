from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.penup()
        self.goto(0, -280)
        self.shape("turtle")
        self.color("purple")

        self.setheading(90)
    def move(self):
        self.forward(10)