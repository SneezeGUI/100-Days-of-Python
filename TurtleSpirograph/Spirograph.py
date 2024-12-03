from turtle import *
import random

turtle = Turtle("turtle")
turtle.color()
turtle.speed(0)

def change_color():
    r = random.random()
    b = random.random()
    g = random.random()

    turtle.pencolor(r, g, b)
walk = True


def spirograph(size_of_gap, circle_size):
    for _ in range(int(360 / size_of_gap)):
        turtle.circle(circle_size)
        turtle.setheading(turtle.heading() + size_of_gap)
        change_color()
## Gap
gap_choice = input("What should the gap between lines be? E.G (5,10,20, etc.): ")
## Circle Size
circle_choice = input("How big should I draw the Circles? Default-100: ")

spirograph(int(gap_choice),int(circle_choice))
screen = Screen()
screen.exitonclick()