from flask import Flask, request, Blueprint, render_template, redirect, session, url_for
from ..models import Task
from ..core import login_required

# create a blueprint
bp = Blueprint('task', __name__)


@bp.route('/task/create', methods=['GET', 'POST'])
@login_required
def create_task():
    if request.method == 'GET':
        # render the create task template
        return render_template('task/create.html')
    else:
        # read values from the form submit
        title = request.form['task-title']
        description = request.form['task-description']

        # create a task document
        task = Task(title = title, description = description)

        # save the tasklist document
        task.save()

        # redirect to the index
        return redirect(url_for('tasklists.view_tasklist'))

@bp.route('/task/delete/<string:tasklist_id>/<string:task_id>', methods=['GET'])
@login_required
def delete_task(tasklist_id, task_id):
    task = Task.query.get_or_404(task_id)
    task.remove()

    # redirect to the index
    return redirect(url_for('tasklists.view_tasklist', tasklist_id = tasklist_id))

@bp.route('/task/update/<string:tasklist_id>/<string:task_id>',methods=['GET','POST'])
@login_required
def update_task(tasklist_id ,task_id):
    task = Task.query.filter(task_id)

    if request.method == 'GET':
        # render the create task template
        return render_template('task/create.html')
    else:
        # read values from the form submit
        title = request.form['task-title']
        description = request.form['task-description']

        title= request.form['title']
        description= request.form['description']
        task.save()

      # redirect to the index
        return redirect(url_for('tasklists.view_tasklist', tasklist_id = tasklist_id))   