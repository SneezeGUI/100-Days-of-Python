# Import Flask module which is a micro web framework written in Python.
from flask import Flask, render_template

# Create an instance of the Flask class we just imported.
app = Flask(__name__)

# The @app.route() decorator binds '/' URL to the home function.
@app.route('/')
def home(): # Function to be called when the user visits the index route of your application.
    return render_template('index.html')

# The following line is used to run the application.
if __name__ == '__main__':
    app.run(debug=True) # When debug is set as True, it reloads itself whenever there's any changes in your code making testing easier.
