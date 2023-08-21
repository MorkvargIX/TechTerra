from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app import config as c
from .view.index import index

# App settings
app = Flask(__name__)
app.register_blueprint(index)

# Database settings
app.config['SQLALCHEMY_DATABASE_URI'] = f'{c.DB_NAME}://{c.DB_USER}:{c.DB_PASSWORD}@{c.DB_HOST}:{c.DB_PORT}/{c.DB_DATABASE}'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

with app.app_context():
    db.create_all()




