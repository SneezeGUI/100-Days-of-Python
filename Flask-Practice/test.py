# TODO: Create the logging_decorator() function 👇

def logging_decorator(function):
    def wrapper(*args):
        result = function(*args)
        print(f'You called \n{function.__name__}({args})')
        print(f'It Returned {result}')
    return wrapper

# TODO: Use the decorator 👇
@logging_decorator
def a_function(*args):
    return sum(args)


a_function(1, 2, 3)

