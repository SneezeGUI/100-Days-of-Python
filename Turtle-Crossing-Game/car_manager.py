from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.all_cars = []
        super().__init__()
        self.hideturtle()
    def spawn_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            rand_y = random.randint(-250, 280)
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(300, rand_y)
            new_car.shapesize(stretch_len=1.5)
            new_car.setheading(180)
            self.all_cars.append(new_car)
    def car_move(self):
       for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE)

