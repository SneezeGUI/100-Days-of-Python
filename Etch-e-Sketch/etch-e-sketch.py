from turtle import Turtle, Screen

tt = Turtle()
screen = Screen()

def move_forward():
    tt.forward(10)
def move_backward():
    tt.back(10)
def clockwise():
    tt.right(10)
def counter_clockwise():
    tt.left(10)
def clear_screen():
    tt.reset()
screen.listen()

screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="a", fun=counter_clockwise)
screen.onkeypress(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()