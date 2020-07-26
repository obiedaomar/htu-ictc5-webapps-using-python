from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/python')
def hello_python():
    return 'Hello, Python!'


@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello, ' + str(name).capitalize()+'!'


@app.route('/multiply2/<int:number>')
def multiply2(number):
    return str(number * 2)
