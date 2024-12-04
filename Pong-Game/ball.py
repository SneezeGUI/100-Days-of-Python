from turtle import Turtle
import random
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 2
        self.y_move = 2
        self.move_speed = 9.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 9.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 9.1
        self.bounce_x()


    # def __init__(self):
    #     super().__init__()
    #     self.shape("circle")
    #     self.color("white")
    #     self.penup()
    #     self.speed(0)
    #
    # def set_heading(self):
    #     rand_heading = random.randint(0, 270)
    #     self.setheading(rand_heading)
    # def hit_wall(self):
    #     number = self.heading()
    #     if number > 0:
    #         number = -number
    #     if number < 0:
    #         number = +number
    #     self.setheading(number)
    # def refresh(self):
    #     x = 0
    #     rand_y = random.randint(-280, 280)
    #     self.goto(x, rand_y)
    #     self.set_heading()
    #
    # def move(self):
    #     self.speed(0)
    #     self.forward(.1)