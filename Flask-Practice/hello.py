from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper
# def make_underlined():
#
# def make_emphasis():



## different routes using the app.decorator
@app.route("/")
@make_bold
@make_emphasis
@make_underlined
def hello_world(): ##you can break to a new line with "\" or """ multi line  text """
    return '<h1 style="text-align: center">Hello</h1>' \
    '<p>This is a Paragraph Element.</p>' \
    '<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fj.gifs.com%2FvgMnVL.gif%3Fdownload%3Dtrue&f=1&nofb=1&ipt=663db8b4488df575d6cd8e976f2ffe2f549dd308cf24772a71066f8bc3250eb2&ipo=images">'\
    '<p>This is another Paragraph Element</p>' \

@app.route('/<name>')
def user_greeting(name):
    return f'Hello {name}!'

@app.route('/bye')
def say_bye():
    return '<p>Bye'

if __name__ == '__main__':
    app.run(debug=True)

# import time
#
# def delay_decorator(function):
#     def wrapper_function():
#         time.sleep(2)
#         #Do something before
#         function()
#         function()
#         #Do something after
#     return wrapper_function
#
# @delay_decorator
# def say_hello():
#     print("Hello")
#
# #With the @ syntactic sugar
# @delay_decorator
# def say_bye():
#     print("Bye")