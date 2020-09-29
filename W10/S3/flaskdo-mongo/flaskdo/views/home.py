from flask import Flask, request, Blueprint, render_template, redirect, session
from ..models import TaskList
# create a blueprint
bp = Blueprint('home', __name__)


@bp.route('/')
def index():
    if request.method == 'GET':
        if 'user'in session:
            tasklists = TaskList.query.filter(TaskList.owner_id == session['user']['id']).all()
    # if request.method == 'GET':
    #     return render_template('tasklist/overdue.html',tasklists=tasklists)
            print(tasklists)
            
            return render_template('index.html', overdue_tasklists =tasklists)

        #print("Is logged in?", session['id'])
    return render_template('index.html')

