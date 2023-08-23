from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Projects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    description = db.Column(db.Text, nullable=False, default='Text about my project')
    started_at = db.Column(db.DateTime(timezone=True), nullable=False)
    ended_at = db.Column(db.DateTime(timezone=True), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=db.func.utcnow())
    updated_at = db.Column(db.DateTime(timezone=True), nullable=True)







