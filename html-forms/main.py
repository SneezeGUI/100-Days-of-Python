from flask import Flask, request, render_template

app= Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    name = request.form['name']
    password = request.form['password']
    return f'Name: {name}, Password: {password}'

if __name__ == '__main__':
    app.run(debug=True)