from flask import render_template
from flask import Blueprint


index = Blueprint('index', __name__, template_folder='templates')


@index.route('/')
def home():
    return render_template('index.html')


@index.route('/about/')
def about():
    return render_template('about.html')