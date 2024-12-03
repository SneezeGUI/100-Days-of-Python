from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
import sys
import os

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_on = True
while game_on:

    screen.update()
    time.sleep(0.1)
    snake.move()

    ##detect collision w food##
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score_refresh()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.game_over()
        game_on = False



    ## detect tail collision##
    for segment in snake.segments[1:]:
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()
screen.exitonclick()