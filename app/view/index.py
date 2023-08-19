from flask import render_template
from . import index


@index.route('/')
@index.route('/index')
def home():
    return render_template('index.html')


@index.route('/about/')
def about():
    return render_template('about.html')


@index.route('/works')
def works():
    return render_template('works.html')


@index.route('/works/add')
def create_form():
    return render_template('create.html')

