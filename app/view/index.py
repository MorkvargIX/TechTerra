from flask import render_template, current_app, request, redirect
from app.models.projects import Projects
from app import db

from . import index


# Main page
@index.route('/')
@index.route('/index')
def home():
    current_app.logger.info('Home endpoint')
    return render_template('index.html')


# About page
@index.route('/about/')
def about():
    current_app.logger.info('About endpoint')
    return render_template('about.html')


# Portfolio page
@index.route('/works/')
def works():
    current_app.logger.info('Works endpoint')
    return render_template('works.html')


# Creating forms
@index.route('/works/add', methods=['POST', 'GET'])
def create_form():
    current_app.logger.info('Form endpoint')
    if request.method == 'POST':
        name = request.form['title']
        description = request.form['text']
        start_date = request.form['startDate']
        end_date = request.form['endDate']

        post = Projects(name=name, description=description, started_at=start_date, ended_at=end_date)

        try:
            db.session.add(post)
            db.session.commit()
            return redirect('/')
        except:
            return '501 error - Try again later'
    return render_template('create.html')

