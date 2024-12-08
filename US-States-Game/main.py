import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()

correct_guesses = []
states_to_learn = []

guessed_right = 0
while guessed_right < 50:
    answer_state = screen.textinput(title= f"Guess the State {guessed_right}/50 ", prompt= "Whats another states name?").title()
    if answer_state in states:
        guessed_right += 1
        correct_guesses.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
    if answer_state == "Exit":
        for state in states:
            if state not in correct_guesses:
                states_to_learn.append(state)
        states_to_learn_csv = pandas.DataFrame(states_to_learn)
        states_to_learn_csv.to_csv("States_to_Learn.csv")
        break


