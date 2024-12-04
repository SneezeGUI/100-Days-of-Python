from turtle import Turtle

class Divider(Turtle):
    def __init__(self):
        super().__init__()
        distance = 700
        self.speed(0)
        self.penup()
        self.pensize(3)
        self.hideturtle()
        self.goto(0,350)
        self.setheading(270)
        self.pencolor("white")
        while distance > 0:
            self.pendown()
            self.forward(15)
            self.penup()
            self.forward(15)
            distance -= 30