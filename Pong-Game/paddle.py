from turtle import Turtle
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.shapesize(stretch_len=4)
        self.color("white")
        self.setheading(90)
        self.penup()
    def move_up(self):
        self.forward(20)
    def move_down(self):
        self.backward(20)