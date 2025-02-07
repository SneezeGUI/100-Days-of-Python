from flask import Flask
import random

app = Flask(__name__)

chosen_number = 0

@app.route('/')
def number_game():
    global chosen_number
    chosen_number = random.randint(0,9)
    print(chosen_number)
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif>'

@app.route('/<int:number>')
def guess_number(number):
    if number == chosen_number:
        return '<h1 style="color: green;">You guessed the right number!</h1>' \
    '<img src=https://tinyurl.com/49kswu5m>'
    elif number < chosen_number:
        return '<h1 style="color: red;">Sorry, that is not correct. Try a higher number.</h1>' \
               '<img src=https://tinyurl.com/ycxhsyap>'
    else:
        return '<h1 style="color: red;">Sorry, that is not correct. Try a lower number.</h1>' \
               '<img src=https://tinyurl.com/ycxhsyap>'





if __name__ == '__main__':
    app.run(debug=True)