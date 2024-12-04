from turtle import Screen
from divider import Divider
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
#Screen Creation
screen = Screen()
screen.setup(width=1200, height =600)
screen.bgcolor("black")
screen.title("Pong - by Sneeze")
screen.tracer(0)
#Game Divider
divider = Divider()
#Scoreboard
scoreboard = Scoreboard()
#Player Paddles
p1 = Paddle()
p1.goto(-585, 0)
p2 = Paddle()
p2.goto(580,0)
#Ball
ball = Ball()

#Player Inputs
screen.listen()
##P1
screen.onkeypress(p1.move_up, "w")
screen.onkeypress(p1.move_down, "s")
##P2
screen.onkeypress(p2.move_up, "Up")
screen.onkeypress(p2.move_down, "Down")
#
game_on = True
while game_on:
    screen.update()
    ball.move()
    #Paddle Collision
    # if ball.distance(p1) <15:
    #     ball.setheading()
    # if ball.distance(p2) <15:
    #     ball.setheading()
    # Wall Collision
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce_y()
     # Detect collision with paddle
    if ball.distance(p2) < 50 and ball.xcor() > 320 or ball.distance(p1) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 620:
        ball.reset_position()
        scoreboard.player_1_scores()

    # Detect L paddle misses:
    if ball.xcor() < -620:
        ball.reset_position()
        scoreboard.player_2_scores()
screen.exitonclick()
