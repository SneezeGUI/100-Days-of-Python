from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Betting", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

#Create 6 turtles
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        #230 is 250 - half the width of the turtle.
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        #Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()























# screen = Screen()
# def speed_select():
#     speed = random.randint(1,10)
# def race():
#     screen.textinput("Bet", "What color will win?")
#     purple.speed(random.randint(1,10))
#     blue.speed(random.randint(1, 10))
#     green.speed(random.randint(1, 10))
#     yellow.speed(random.randint(1, 10))
#     orange.speed(random.randint(1, 10))
#     red.speed(random.randint(1, 10))
#
#
# start_pos_x = (-450)
# start_pos_y = (150)
#
#
#
# purple = Turtle("turtle")
# purple.color("purple")
# purple.penup()
# purple.goto(start_pos_x, start_pos_y)
#
#
# blue = Turtle("turtle")
# blue.color("blue")
# blue.penup()
# blue.goto(start_pos_x, start_pos_y -50)
#
# green = Turtle("turtle")
# green.color("green")
# green.penup()
# green.goto(start_pos_x, start_pos_y -100)
#
# yellow = Turtle("turtle")
# yellow.color("yellow")
# yellow.penup()
# yellow.goto(start_pos_x, start_pos_y -150)
#
# orange = Turtle("turtle")
# orange.color("orange")
# orange.penup()
# orange.goto(start_pos_x, start_pos_y -200)
#
# red = Turtle("turtle")
# red.color("red")
# red.penup()
# red.goto(start_pos_x, start_pos_y - 250)
#
# race()
#
# print(purple.speed())
# screen.exitonclick()