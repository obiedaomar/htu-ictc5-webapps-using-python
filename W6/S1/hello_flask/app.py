from flask import Flask  # import flask
import random

app = Flask(__name__)  # create a new flask application

# define basic routes


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/hello')
def say_hello():
    return 'Welcome to Python web!'


@app.route('/magic8')
def magic_8():
    rndx = random.randint(1, 10)
    return f"Your lucky number is {rndx}."


@app.route('/greet/<name>')
def greet(name):
    return 'Hello, ' + str(name).capitalize() + '!'


# run your flask application

if __name__ == "__main__":  # on running python app.py
    app.run()  # run the flask app
