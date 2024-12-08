# from turtle import Turtle
# import pandas
# data = pandas.read_csv("50_states.csv")
#
# class States(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.data = pandas.read_csv("50_states.csv")
#         self.states = self.data["state"]
#         self.start_y = self.data["y"]
#         self.start_x = self.data["x"]
#         self.state_turtles = []
#
#     def populate_states(self):
#         for state in self.states:
#             state = Turtle()
#             self.shape("turtle")
#             self.color("black")
#             # self.hideturtle()
#             self.penup()
#             self.speed(0)
#             self.goto(self.start_x, self.start_y)
#             self.state_turtles.append(state)
#
#     def guess(self):
#         guess = input("Guess a State: ")
#         if guess in self.states:
#             guess = Turtle()
#             self.shape("turtle")
#             self.penup()
#             self.speed(0)
#             self.goto(self.start_x, self.start_y)
#             print(self.data[f"{guess}"])
# guess = input("?")
# if guess in data["state"]:
#     print("yes")

    # def reveal(self):
    #     if guess in self.state_turtles:
    #         self.write(f"{}", move=False, align="center", font=("Arial", 12, "bold"))
