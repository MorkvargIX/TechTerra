import base64
import json
import codecs

from flask import render_template, current_app, request, redirect
from sqlalchemy.exc import SQLAlchemyError
from app.models.models import Projects
from app import db
from ..api import weather

from . import index


# Main page
@index.route('/')
@index.route('/index')
def home():
    current_app.logger.info('Home endpoint')
    forecast = weather.weather_api()

    return render_template('index.html', forecast=forecast)


# About page
@index.route('/about/')
def about():
    current_app.logger.info('About endpoint')
    return render_template('about.html')


# Portfolio page
@index.route('/works/')
def works():
    current_app.logger.info('Works endpoint')
    projects = Projects.query.all()
    return render_template('works.html', projects=projects, image_to_base64=image_to_base64)


def image_to_base64(image_data):
    return base64.b64encode(image_data).decode('utf-8')


# Creating forms
@index.route('/works/add', methods=['POST', 'GET'])
def create_form():
    current_app.logger.info('Form endpoint')
    if request.method == 'POST':
        name = request.form['title']
        description = request.form['text']
        start_date = request.form['startDate']
        end_date = request.form['endDate']
        image = request.files['image'].read()

        post = Projects(name=name, description=description, image=image, started_at=start_date, ended_at=end_date)

        try:
            db.session.add(post)
            db.session.commit()
            return redirect('/')
        except SQLAlchemyError:
            db.session.rollback()
            return '501 error - Try again later'

    return render_template('create.html')

