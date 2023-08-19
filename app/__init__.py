import config as c

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .view.index import index

app = Flask(__name__)
app.register_blueprint(index)


app.config['SQLALCHEMY_DATABASE_URI'] = f'{c.DB_NAME}://{c.DB_USER}:{c.DB_PASSWORD}@{c.DB_HOST}:{c.DB_PORT}/{c.DB_DATABASE}'
db = SQLAlchemy(app)




