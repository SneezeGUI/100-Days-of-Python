import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

#screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#player obj
player = Player()

#scoreboard
scoreboard = Scoreboard()
car_manager = CarManager()

## Player Input
screen.listen()
screen.onkeypress(player.move, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.spawn_car()
    car_manager.car_move()

#Player reaches end check
    if player.ycor() > 290:
        scoreboard.new_level()
        player.goto(0, -280)
        game_is_on = True

#Player is Hit by car check
    for car in car_manager.all_cars:
        if player.distance(car) < 15:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()