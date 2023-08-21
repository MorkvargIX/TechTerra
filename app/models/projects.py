from app import db


class Projects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=False, nullable=False)
    description = db.Column(db.Text, unique=False, nullable=False, default='Text about my project')



