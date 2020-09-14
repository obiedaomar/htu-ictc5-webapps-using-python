from flask import Flask, request, Blueprint, render_template, redirect, session

# create a blueprint
bp = Blueprint('home', __name__)


@bp.route('/')
def index():
    if request.method == 'GET':
        return render_template('index.html')
