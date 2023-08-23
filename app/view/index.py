from flask import render_template, current_app, request, redirect
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


@index.route('/works/add', methods=['POST', 'GET'])
def create_form():
    current_app.logger.info('Form endpoint')
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']
        start_date = request.form['startDate']
        end_date = request.form['endDate']
        return redirect('/')
    return render_template('create.html')

