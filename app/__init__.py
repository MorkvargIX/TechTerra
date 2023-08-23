from flask import Flask
from flask_migrate import Migrate
from app.models.projects import db

from app import config as c
from app.view.index import index


# App settings
app = Flask(__name__)
app.register_blueprint(index)

# Database settings
app.config['SQLALCHEMY_DATABASE_URI'] = f'{c.db_name}://{c.db_user}:{c.db_password}@{c.db_host}:{c.db_port}/{c.db_database}'
db.init_app(app)
migrate = Migrate(app, db)





