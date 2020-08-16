import os
from flask import Flask, render_template, flash, redirect, url_for, Markup, request

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'secret string')

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        print(username, password)

        # if valid_login(request.form['username'],
        #     request.form['password']):
        #     return log_the_user_in(request.form['username'])
        # else:
        #     error = 'Invalid username/password'
    
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)

# run your flask application
if __name__ == "__main__":  # on running python app.py
    app.run(debug=True)  # run the flask app
