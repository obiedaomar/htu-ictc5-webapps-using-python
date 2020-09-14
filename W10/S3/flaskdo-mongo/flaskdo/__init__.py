import os

from flask import Flask, session
from .core import db, intialize_db_config

# create the Flask
app = Flask(__name__)

# configure the app
app.config.from_mapping(
    SECRET_KEY='dev'
)

intialize_db_config(app)

# a simple test route
@app.route('/hello')
def hello():
    return 'Hello, World!'

# register template global function
@app.template_global()
def is_logged_in():
    if 'user' in session:
        return user
    return None

@app.template_global()
def get_first_name():
    if 'user' in session:
        return session['user']['first_name']
    else:
        return None

# register the 'user' blueprint
from .views import user
app.register_blueprint(user.bp)

# register the 'home' blueprint
from .views import home
app.register_blueprint(home.bp)

# register the 'tasklists' blueprint
from .views import tasklists
app.register_blueprint(tasklists.bp)