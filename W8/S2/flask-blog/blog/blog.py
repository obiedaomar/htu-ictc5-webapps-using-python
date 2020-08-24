from flask import Blueprint, render_template
from blog.db import get_db

# define our blueprint
bp = Blueprint('blog', __name__)


@bp.route('/')
@bp.route('/posts')
def index():
    
    # get the DB connection
    db = get_db()

    # retrieve all posts
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()

    # render 'blog' blueprint with posts
    return render_template('blog/index.html', posts=posts)

@bp.route('/add/post')
def add_post():
    # write your code here :)!
    
    # render 'add-post.html'
    return render_template('blog/add-post.html')