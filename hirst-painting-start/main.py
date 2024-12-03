# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
import turtle
from turtle import Turtle, Screen
import random

user_x = int(input("Please input Grid X Size: "))
user_y = int(input("Please input Grid X Size: "))

tt = Turtle()
tt.speed(0)
screen = Screen()
tt.shape("circle")
tt.pensize(20)
tt.screen.colormode(255)
tt.screen.colormode()
tt.penup()
printed_dots = 0
start_pos_x = (-250)
start_pos_y = (-250)
tt.goto(start_pos_x, start_pos_y)

def change_color():
    color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
                  (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
                  (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
                  (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
                  (176, 192, 208), (168, 99, 102)]
    color_select = random.choice(color_list)
    r = int(color_select[0])
    b = int(color_select[1])
    g = int(color_select[2])

    tt.color(r, g, b)

def paint (grid_x, grid_y):
    global start_pos_y
    global printed_dots

    while printed_dots < grid_x * grid_y:
        for _ in range(grid_x):
            change_color()
            tt.stamp()
            tt.penup()
            tt.forward(50)
            printed_dots += 1

            print(printed_dots)

        for _ in range(grid_y):
            start_pos_y += 50
            tt.goto(start_pos_x, start_pos_y)
            paint(grid_x, grid_y)
# change_color()
# tt.forward(10)


paint(user_x, user_y)
screen.exitonclick()

