from flask import Flask, request, Blueprint, render_template, redirect, session, url_for
from ..models import TaskList, User

# create a blueprint
bp = Blueprint('tasklists', __name__)


@bp.route('/tasklist/create', methods=['GET', 'POST'])
def create_tasklist():
    if request.method == 'GET':
        # render the create tasklist template
        return render_template('tasklist/create.html')
    else:
        # read values from the form submit
        name = request.form['list-name']
        description = request.form['list-description']

        # create a tasklist document
        tasklist = TaskList(name = name, description = description)

        # save the tasklist document
        tasklist.save()

        # get the logged in user
        user = User.query.get_or_404(session['user']['id'])

        # add the newly created tasklist
        user.add_tasklist(str(tasklist.mongo_id))

        # save the changes to the user object
        user.save()

        # update the session
        session['user'] = user.serialized

        # redirect to the index
        return redirect(url_for('tasklists.tasklists'))


@bp.route('/tasklist/<string:tasklist_id>')
def view_tasklist(tasklist_id):
    tasklist = TaskList.query.get_or_404(tasklist_id)
    return render_template('tasklist/view.html', tasklist = tasklist)

@bp.route('/tasklist/delete/<string:tasklist_id>')
def delete_tasklist(tasklist_id):
    # retrieve the tasklist
    tasklist = TaskList.query.get_or_404(tasklist_id)
    
    # remove the id from the user tasklists in session
    tasklists = list(session['user']['tasklists'])
    tasklists.remove(tasklist_id)
    session['user']['tasklists'] = tasklists

    # delete the tasklist
    tasklist.remove()
    
    # redirect the user to the tasklists
    return redirect(url_for('tasklists.tasklists'))


@bp.route('/tasklists')
def tasklists():    
    # get the list of tasklist ids
    tasklist_ids = session['user']['tasklists']

    # create a list to store the tasklists
    tasklists = list()
    
    # append tasklists to tasklists based on their ids
    for tasklist_id in tasklist_ids:
        tasklists.append(TaskList.query.get(tasklist_id))
    
    # render the task lists template
    return render_template('tasklist/task-lists.html', tasklists = tasklists)


# @bp.route('/user/update/<int:user_id>', methods=['POST'])
# def update_user(user_id):
#     user = User.query.get(user_id)
#     form = UserForm()
#     if form.validate_on_submit():
#         form.instance = user
#         form.save()
#         return redirect(url_for('list_user'))
#     form = UserForm(document=user)
#     return render_template('/user/edit.html', form=form, user=user)
