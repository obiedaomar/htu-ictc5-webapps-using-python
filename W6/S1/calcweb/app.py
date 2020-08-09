# calcweb

from flask import Flask             # import flask

app = Flask(__name__)               # create a new flask application

# define basic routes


@app.route('/add/<n1>/<n2>')
def add(n1, n2):
    return f'{n1} + {n2} = {int(n1) + int(n2)}'


# run your flask application

if __name__ == "__main__":        # on running python app.py
    app.run(debug=True)           # run the flask app
