import os

from flask import current_app, Blueprint, render_template, request

main = Blueprint('main', __name__, url_prefix='/')

@main.route('/', methods=('GET', 'POST'))
def index():
    return render_template('index.html')
