from flask import Flask
from flask_migrate import Migrate
from app.models.projects import db

from app import config as c
from app.view.index import index


# App settings
app = Flask(__name__)
app.register_blueprint(index)

# Database settings
app.config['SQLALCHEMY_DATABASE_URI'] = f'{c.DB_NAME}://{c.DB_USER}:{c.DB_PASSWORD}@{c.DB_HOST}:{c.DB_PORT}/{c.DB_DATABASE}'
db.init_app(app)
migrate = Migrate(app, db)





