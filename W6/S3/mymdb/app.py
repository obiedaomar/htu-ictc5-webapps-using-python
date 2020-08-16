import os
from flask import Flask, render_template, flash, redirect, url_for, Markup

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'secret string')

site = {
    'name':'MyMDB'
}

# declare user dictionary
user = {
    'username': 'Python Web',
    'bio': 'We love Python.',
}

# declare list of movies
movies = [
    {'name': 'My Neighbor Totoro', 'year': '1988'},
    {'name': 'Three Colours trilogy', 'year': '1993'},
    {'name': 'Forrest Gump', 'year': '1994'},
    {'name': 'Perfect Blue', 'year': '1997'},
    {'name': 'The Matrix', 'year': '1999'},
    {'name': 'Memento', 'year': '2000'},
    {'name': 'The Bucket list', 'year': '2007'},
    {'name': 'Black Swan', 'year': '2010'},
    {'name': 'Gone Girl', 'year': '2014'},
    {'name': 'CoCo', 'year': '2017'},
]


@app.route('/watchlist')
def watchlist():
    return render_template('watchlist.html', user=user, movies=movies, site=site)


@app.route('/')
def index():
    return render_template('index.html', site=site)


# register template global function
@app.template_global()
def global_message():
    return 'I am global message.'


# register template filter
@app.template_filter()
def musical(s):
    return s + Markup(' &#9835;')


@app.route('/watchlist2')
def watchlist_with_static():
    return render_template('watchlist_with_static.html', user=user, movies=movies, site=site)


# message flashing
@app.route('/flash')
def just_flash():
    flash('I am Flash, who is looking for me?')
    # flash('I am Flash, again.')

    return redirect(url_for('index'))


# 404 error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


# 500 error handler
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500