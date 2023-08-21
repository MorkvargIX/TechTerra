from flask import render_template, current_app
from . import index


@index.route('/')
@index.route('/index')
def home():
    current_app.logger.info('Home endpoint')
    return render_template('index.html')


@index.route('/about/')
def about():
    current_app.logger.info('About endpoint')
    return render_template('about.html')


@index.route('/works/')
def works():
    current_app.logger.info('Works endpoint')
    return render_template('works.html')


@index.route('/works/add')
def create_form():
    current_app.logger.info('Form endpoint')
    return render_template('create.html')

